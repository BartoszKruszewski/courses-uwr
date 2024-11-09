using System;
using System.Collections.Generic;
using System.Linq;
using System.Web;
using System.Web.UI;
using System.Web.UI.WebControls;

namespace WebApplication1
{
    public partial class Login : System.Web.UI.Page
    {
        protected void btnLogin_Click(object sender, EventArgs e)
        {
            string username = txtUsername.Text;
            string password = txtPassword.Text;

            // Sprawdź poprawność danych logowania (tutaj powinno być połączenie z bazą danych)
            if (IsValidUser(username, password))
            {
                // Zapisz użytkownika w sesji
                Session["User"] = username;

                // Przekierowanie do oryginalnej strony, z której użytkownik próbował uzyskać dostęp
                string returnUrl = Session["ReturnUrl"] as string;
                if (!string.IsNullOrEmpty(returnUrl))
                {
                    Response.Redirect(returnUrl);
                }
                else
                {
                    // Jeśli nie ma ścieżki, przekieruj na stronę główną
                    Response.Redirect("Protected.aspx");
                }
            }
            else
            {
                // Obsługa błędnych danych logowania
                lblError.Text = "Niepoprawny login lub hasło.";
            }
        }

        // Funkcja sprawdzająca poprawność użytkownika (przykład)
        private bool IsValidUser(string username, string password)
        {
            // Logika sprawdzania danych (np. z bazy danych)
            return username == "admin" && password == "password"; // Przykład
        }
    }
}