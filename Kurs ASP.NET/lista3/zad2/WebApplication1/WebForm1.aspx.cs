using System;
using System.Collections.Generic;
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
            if (Session["CookiesEnabled"] == null)
            {
                HttpCookie testCookie = new HttpCookie("TestCookie", "test");
                Response.Cookies.Add(testCookie);

                Session["CookiesEnabled"] = false;
            }
            else
            {
                if (Request.Cookies["TestCookie"] != null)
                {
                    Session["CookiesEnabled"] = true;
                    lblMessage.Text = "Ciasteczka są obsługiwane.";
                }
                else
                {
                    Session["CookiesEnabled"] = false;
                    lblMessage.Text = "Ciasteczka nie są obsługiwane.";
                }
            }
        }

        protected void btnAddCookie_Click(object sender, EventArgs e)
        {
            HttpCookie myCookie = new HttpCookie("UserSettings");
            myCookie["Theme"] = "Dark";
            myCookie["FontSize"] = "Medium";
            myCookie.Expires = DateTime.Now.AddDays(7);
            Response.Cookies.Add(myCookie);
            lblMessage.Text = "Ciasteczko zostało dodane.";
        }

        protected void btnReadCookie_Click(object sender, EventArgs e)
        {
            HttpCookie retrievedCookie = Request.Cookies["UserSettings"];
            if (retrievedCookie != null)
            {
                string theme = retrievedCookie["Theme"];
                string fontSize = retrievedCookie["FontSize"];
                lblMessage.Text = $"Odczytano ciasteczko: Theme = {theme}, FontSize = {fontSize}";
            }
            else
            {
                lblMessage.Text = "Nie znaleziono ciasteczka 'UserSettings'.";
            }
        }

        protected void btnDeleteCookie_Click(object sender, EventArgs e)
        {
            if (Request.Cookies["UserSettings"] != null)
            {
                HttpCookie deleteCookie = new HttpCookie("UserSettings");
                deleteCookie.Expires = DateTime.Now.AddDays(-1);
                Response.Cookies.Add(deleteCookie);
                lblMessage.Text = "Ciasteczko zostało usunięte.";
            }
            else
            {
                lblMessage.Text = "Nie znaleziono ciasteczka 'UserSettings'.";
            }
        }
    }
}