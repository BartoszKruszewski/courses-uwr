<%@ Page Language="C#" AutoEventWireup="true" CodeBehind="WebForm1.aspx.cs" Inherits="WebApplication1.WebForm1" %>

<!DOCTYPE html>

<html xmlns="http://www.w3.org/1999/xhtml">
<head runat="server">
    <title></title>
</head>
<body>
    <form id="form1" runat="server">
        <div>
            <h2>Odczyt danych z pliku konfiguracyjnego:</h2>
            <asp:Label ID="lblAppTitle" runat="server" Text=""></asp:Label><br />
            <asp:Label ID="lblVersion" runat="server" Text=""></asp:Label><br />
            <asp:Label ID="lblConnectionString" runat="server" Text=""></asp:Label><br />
        </div>
    </form>
</body>
</html>
