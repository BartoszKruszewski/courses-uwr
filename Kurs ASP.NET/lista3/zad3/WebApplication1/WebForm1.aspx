<%@ Page Language="C#" AutoEventWireup="true" CodeBehind="WebForm1.aspx.cs" Inherits="WebApplication1.WebForm1" %>

<!DOCTYPE html>

<html xmlns="http://www.w3.org/1999/xhtml">
<head runat="server">
    <title></title>
</head>
<body>
    <form id="form1" runat="server">
        <div>
            <h3>Informacje o żądaniu:</h3>
            <asp:Label ID="lblUserAgent" runat="server" Text=""></asp:Label><br />
            <asp:Label ID="lblClientIp" runat="server" Text=""></asp:Label><br />

            <h3>Ścieżka fizyczna:</h3>
            <asp:Label ID="lblPhysicalPath" runat="server" Text=""></asp:Label><br />

            <h3>Niestandardowy nagłówek odpowiedzi:</h3>
            <asp:Label ID="lblCustomHeader" runat="server" Text="Dodano niestandardowy nagłówek odpowiedzi!"></asp:Label><br />

            <h3>Ścieżka żądania:</h3>
            <asp:Label ID="lblRequestPath" runat="server" Text=""></asp:Label>
        </div>
    </form>
</body>
</html>
