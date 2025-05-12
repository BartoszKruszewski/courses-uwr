using System;

abstract class Node
{
    public abstract int Accept(IVisitor visitor);
}

class Leaf : Node
{
    public override int Accept(IVisitor visitor)
    {
        return visitor.VisitLeaf(this);
    }
}

class Branch : Node
{
    public Node Left { get; }
    public Node Right { get; }

    public Branch(Node left, Node right)
    {
        Left = left;
        Right = right;
    }

    public override int Accept(IVisitor visitor)
    {
        return visitor.VisitBranch(this);
    }
}

interface IVisitor
{
    int VisitLeaf(Leaf leaf);
    int VisitBranch(Branch branch);
}

class DepthVisitor : IVisitor
{
    public int VisitLeaf(Leaf leaf)
    {
        return 1;
    }

    public int VisitBranch(Branch branch)
    {
        int leftDepth = branch.Left.Accept(this);
        int rightDepth = branch.Right.Accept(this);
        return 1 + Math.Max(leftDepth, rightDepth);
    }
}

//        B
//       / \
//      L   B
//         / \
//        L   L
Node tree = new Branch(
    new Leaf(),
    new Branch(
        new Leaf(),
        new Leaf()
    )
);

IVisitor depthVisitor = new DepthVisitor();
int depth = tree.Accept(depthVisitor);

Console.WriteLine(depth);