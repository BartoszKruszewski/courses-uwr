using System;
using System.Collections.Generic;
using System.Linq;
using System.Web;
using System.Web.Security;
using System.Web.SessionState;

namespace WebApplication1
{
    public class Global : System.Web.HttpApplication
    {

        protected void Application_Start(object sender, EventArgs e)
        {

        }

        protected void Session_Start(object sender, EventArgs e)
        {

        }

        protected void Application_BeginRequest(object sender, EventArgs e)
        {
            HttpContext context = HttpContext.Current;
            string path = context.Request.Path;

            // Sprawdź, czy sesja jest zainicjalizowana
            if (context.Session != null)
            {
                // Sprawdź, czy użytkownik jest na stronie logowania
                if (!path.EndsWith("Login.aspx"))
                {
                    // Sprawdź, czy użytkownik jest zalogowany
                    if (context.Session["User"] == null)
                    {
                        // Zapisz ścieżkę, z której użytkownik próbował uzyskać dostęp
                        context.Session["ReturnUrl"] = path;

                        // Przekierowanie do strony logowania
                        context.Response.Redirect("Login.aspx");
                    }
                }
            }
        }

        protected void Application_AuthenticateRequest(object sender, EventArgs e)
        {

        }

        protected void Application_Error(object sender, EventArgs e)
        {

        }

        protected void Session_End(object sender, EventArgs e)
        {

        }

        protected void Application_End(object sender, EventArgs e)
        {

        }
    }
}