<%@ Page Language="C#" AutoEventWireup="true" CodeBehind="start.aspx.cs" Inherits="zad4.start" %>

<!DOCTYPE html>

<html xmlns="http://www.w3.org/1999/xhtml">
<head runat="server">
    <title>Formularz zgłoszenia</title>
</head>
<body>
    <form id="form1" runat="server">
        <div>
            <h2>Formularz zgłoszenia</h2>

            Imię i nazwisko: <asp:TextBox ID="txtName" runat="server" /><br />
            Data: <asp:TextBox ID="txtDate" runat="server" TextMode="Date" /><br />
            Nazwa zajęć: <asp:TextBox ID="txtCourse" runat="server" /><br />
            Numer zestawu: <asp:TextBox ID="txtSetNumber" runat="server" /><br />

            <h3>Wyniki zadań:</h3>
            <div class="task" id="TaskPanel" runat="server">

            </div>
            <asp:Button ID="btnSubmit" Text="Zatwierdź" runat="server" OnClick="btnSubmit_Click" />
            <asp:Label ID="lblError" runat="server" ForeColor="Red" Visible="false" />
        </div>
    </form>
</body>
</html>
