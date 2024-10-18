<%@ Page Language="C#" AutoEventWireup="true" CodeBehind="WebForm1.aspx.cs" Inherits="WebApplication1.WebForm1" %>

<!DOCTYPE html>

<html xmlns="http://www.w3.org/1999/xhtml">
<head runat="server">
    <title>Example</title>
</head>
<body>
    <h1>To jest przykładowa strona ASP.NET</h1>
    <p>Treść statyczna bez interakcji użytkownika.</p>

    <form id="form1" runat="server">
        <div>
            <asp:TextBox ID="txtName" runat="server" Placeholder="Wpisz swoje imię"></asp:TextBox>
            <asp:Button ID="btnSubmit" runat="server" Text="Wyślij" OnClick="btnSubmit_Click" />
        </div>
    </form>
</body>
</html>
