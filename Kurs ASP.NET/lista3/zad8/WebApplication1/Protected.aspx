<%@ Page Language="C#" AutoEventWireup="true" CodeBehind="Protected.aspx.cs" Inherits="WebApplication1.Home" %>

<!DOCTYPE html>

<html xmlns="http://www.w3.org/1999/xhtml">
<head runat="server">
    <title></title>
</head>
<body>
    <form id="form1" runat="server">
        <div>
            <h1>Witaj, <%: Session["User"] %>!</h1>
            <p>To jest strona główna aplikacji.</p>
        </div>
    </form>
</body>
</html>
