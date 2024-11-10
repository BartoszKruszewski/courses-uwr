using System;
using System.Collections.Generic;
using System.Configuration;
using System.Linq;
using System.Web;
using System.Web.UI;
using System.Web.UI.WebControls;

namespace WebApplication1
{
    public partial class WebForm1 : System.Web.UI.Page
    {
        protected void Page_Load(object sender, EventArgs e)
        {
            // Odczyt z appSettings
            string appTitle = ConfigurationManager.AppSettings["AppTitle"];
            string version = ConfigurationManager.AppSettings["Version"];

            // Odczyt z connectionStrings
            var connectionString = ConfigurationManager.ConnectionStrings["DefaultConnection"]?.ConnectionString;

            // Wyświetlenie danych na stronie
            lblAppTitle.Text = $"Tytuł aplikacji: {appTitle}";
            lblVersion.Text = $"Wersja: {version}";
            lblConnectionString.Text = $"Connection String: {connectionString}";
        }
    }
}