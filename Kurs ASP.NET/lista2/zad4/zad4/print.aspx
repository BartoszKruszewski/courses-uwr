<%@ Page Language="C#" AutoEventWireup="true" CodeBehind="print.aspx.cs" Inherits="zad4.print" %>

<!DOCTYPE html>

<html xmlns="http://www.w3.org/1999/xhtml">
<head runat="server">
    <title>Formularz wydruku</title>
</head>
<body>
    <div>
        <h2>Podsumowanie zgłoszenia</h2>

        <table border="1">
            <tr><th>Imię i nazwisko</th><td><%= Request.QueryString["name"] %></td></tr>
            <tr><th>Data</th><td><%= Request.QueryString["date"] %></td></tr>
            <tr><th>Nazwa zajęć</th><td><%= Session["Course"] %></td></tr>
            <tr><th>Numer zestawu</th><td><%= Session["SetNumber"] %></td></tr>

            <tr><th colspan="2">Wyniki zadań</th></tr>
            <% for (int i = 1; i <= 10; i++) { %>
                <tr><td>Zadanie <%= i %></td><td><%= Session[$"Task{i}"] ?? "0" %></td></tr>
            <% } %>
        </table>
    </div>
</body>
</html>
