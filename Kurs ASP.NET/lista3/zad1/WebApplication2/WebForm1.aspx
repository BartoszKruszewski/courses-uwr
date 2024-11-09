<%@ Page Language="C#" AutoEventWireup="true" CodeBehind="WebForm1.aspx.cs" Inherits="WebApplication2.WebForm1" %>

<!DOCTYPE html>

<html xmlns="http://www.w3.org/1999/xhtml">
<head runat="server">
    <title></title>
</head>
<body>
    <form id="postForm" action="res.aspx" method="post" style="display: none;">
        <input type="hidden" name="p1" value="v1" />
        <input type="hidden" name="p2" value="v2" />
    </form>

    <a href="#" onclick="document.getElementById('postForm').submit(); return false;">
        POST
    </a>

    <button type="button" onclick="document.location.href='res.aspx?p1=v1&p2=v2';">
        GET
    </button>


</body>
</html>
