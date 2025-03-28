#load "TestRunner.csx"
#r "nuget: MSTest.TestFramework, 3.1.0"
#r "nuget: MSTest.TestAdapter, 3.1.0"

using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using System.Text;
using Microsoft.VisualStudio.TestTools.UnitTesting;


public class TagBuilder
{
    private readonly string _tagName;
    private readonly TagBuilder _parent;
    private readonly StringBuilder _body = new StringBuilder();
    private readonly Dictionary<string, string> _attributes = new Dictionary<string, string>();
    public bool IsIndented { get; set; }
    public int Indentation { get; set; } = 4;
    private int _currentLevel;

    public TagBuilder() { }
    public TagBuilder(string tagName, TagBuilder parent)
    {
        _tagName = tagName;
        _parent = parent;
        if (parent != null)
        {
            IsIndented = parent.IsIndented;
            Indentation = parent.Indentation;
            _currentLevel = parent._currentLevel + 1;
        }
    }

    public TagBuilder AddContent(string content)
    {
        _body.Append(content);
        return this;
    }

    public TagBuilder AddContentFormat(string format, params object[] args)
    {
        _body.AppendFormat(format, args);
        return this;
    }

    public TagBuilder StartTag(string tagName)
    {
        return new TagBuilder(tagName, this);
    }

    public TagBuilder EndTag()
    {
        _parent?.AddContent(ToString());
        return _parent;
    }

    public TagBuilder AddAttribute(string name, string value)
    {
        _attributes[name] = value;
        return this;
    }

    public override string ToString()
    {
        if (string.IsNullOrEmpty(_tagName) && _body.Length > 0) return _body.ToString();
        var sb = new StringBuilder();
        if (IsIndented && !string.IsNullOrEmpty(_tagName)) sb.Append(GetIndentationString(_currentLevel));
        if (!string.IsNullOrEmpty(_tagName))
        {
            sb.Append("<");
            sb.Append(_tagName);
            if (_attributes.Any())
            {
                sb.Append(" ");
                sb.Append(string.Join(" ", _attributes.Select(kvp => $"{kvp.Key}='{kvp.Value}'")));
            }
        }
        if (_body.Length == 0)
        {
            if (!string.IsNullOrEmpty(_tagName))
            {
                sb.Append("/>");
                if (IsIndented) sb.AppendLine();
            }
        }
        else
        {
            if (!string.IsNullOrEmpty(_tagName)) sb.Append(">");
            bool hasChildTag = _body.ToString().Contains("<");
            if (hasChildTag && IsIndented) sb.AppendLine();
            if (hasChildTag && IsIndented)
            {
                var lines = _body.ToString().Split(new[] { "\r\n", "\n" }, StringSplitOptions.None);
                foreach (var line in lines)
                {
                    if (!string.IsNullOrWhiteSpace(line)) sb.Append(GetIndentationString(_currentLevel + 1));
                    sb.AppendLine(line);
                }
            }
            else
            {
                sb.Append(_body);
            }
            if (!string.IsNullOrEmpty(_tagName))
            {
                if (hasChildTag && IsIndented) sb.Append(GetIndentationString(_currentLevel));
                sb.Append("</");
                sb.Append(_tagName);
                sb.Append(">");
                if (IsIndented) sb.AppendLine();
            }
        }
        return sb.ToString();
    }

    private string GetIndentationString(int level)
    {
        return new string(' ', level * Indentation);
    }
}

[TestClass]
public class Tests
{
    [TestMethod]
    public void EmptyTagNoIndentation()
    {
        var builder = new TagBuilder();
        builder.StartTag("img").AddAttribute("src", "example.png").EndTag();
        Assert.AreEqual("<img src='example.png'/>", builder.ToString());
    }

    [TestMethod]
    public void SingleTagWithContentNoIndent()
    {
        var builder = new TagBuilder();
        builder.StartTag("div").AddAttribute("class", "my-div").AddContent("Hello").EndTag();
        Assert.AreEqual("<div class='my-div'>Hello</div>", builder.ToString());
    }

    [TestMethod]
    public void NestedTagsWithIndentation()
    {
        var builder = new TagBuilder { IsIndented = true, Indentation = 2 };
        builder.StartTag("ul")
            .StartTag("li").AddContent("Item1").EndTag()
            .StartTag("li").AddContent("Item2").EndTag()
        .EndTag();
        var result = builder.ToString();
        StringAssert.Contains(result, "<ul>");
        StringAssert.Contains(result, "  <li>Item1</li>");
        StringAssert.Contains(result, "  <li>Item2</li>");
        StringAssert.Contains(result, "</ul>");
    }

    [TestMethod]
    public void EmptyParentTagWithIndentation()
    {
        var builder = new TagBuilder { IsIndented = true, Indentation = 2 };
        builder.StartTag("div").AddAttribute("id", "container").EndTag();
        var result = builder.ToString();
        StringAssert.Contains(result, "<div id='container'/>");
    }

    [TestMethod]
    public void MultipleSiblingsWithIndentation()
    {
        var builder = new TagBuilder { IsIndented = true, Indentation = 2 };
        builder
            .StartTag("section").AddAttribute("class", "main")
                .StartTag("p").AddContent("Paragraph content").EndTag()
                .StartTag("p").AddContent("Second paragraph").EndTag()
            .EndTag()
            .StartTag("footer").AddContent("Footer content").EndTag();
        var result = builder.ToString();
        StringAssert.Contains(result, "<section class='main'>");
        StringAssert.Contains(result, "  <p>Paragraph content</p>");
        StringAssert.Contains(result, "  <p>Second paragraph</p>");
        StringAssert.Contains(result, "</section>");
        StringAssert.Contains(result, "<footer>Footer content</footer>");
    }
}

var tests = new Tests();

Run(tests.EmptyTagNoIndentation);
Run(tests.SingleTagWithContentNoIndent);
Run(tests.NestedTagsWithIndentation);
Run(tests.EmptyParentTagWithIndentation);
Run(tests.MultipleSiblingsWithIndentation);

var root = new TagBuilder { IsIndented = true, Indentation = 2 };
root
.StartTag("parent")
    .AddAttribute("parentproperty1", "true")
    .AddAttribute("parentproperty2", "5")
    .StartTag("child1")
        .AddAttribute("childproperty1", "c")
        .AddContent("childbody")
    .EndTag()
    .StartTag("child2")
        .AddAttribute("childproperty2", "c")
        .AddContent("childbody")
    .EndTag()
.EndTag()
.StartTag("script")
    .AddContent("$.scriptbody();")
.EndTag();
Console.WriteLine(root.ToString());
