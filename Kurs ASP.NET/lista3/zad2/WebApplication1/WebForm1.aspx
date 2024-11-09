<%@ Page Language="C#" AutoEventWireup="true" CodeBehind="WebForm1.aspx.cs" Inherits="WebApplication1.WebForm1" %>

<!DOCTYPE html>

<html xmlns="http://www.w3.org/1999/xhtml">
<head runat="server">
    <title></title>
</head>
<body>
    <form id="form1" runat="server">
        <div>
            <asp:Label ID="lblMessage" runat="server" Text=""></asp:Label><br />
            <asp:Button ID="btnAddCookie" runat="server" Text="Add Cookie" OnClick="btnAddCookie_Click" /><br />
            <asp:Button ID="btnReadCookie" runat="server" Text="Read Cookie" OnClick="btnReadCookie_Click" /><br />
            <asp:Button ID="btnDeleteCookie" runat="server" Text="Delete Cookie" OnClick="btnDeleteCookie_Click" /><br />
        </div>
    </form>
</body>
</html>
