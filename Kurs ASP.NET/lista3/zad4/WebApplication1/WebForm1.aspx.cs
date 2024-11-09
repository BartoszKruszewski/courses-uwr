using System;
using System.Collections.Generic;
using System.Linq;
using System.Web;
using System.Web.Services.Description;
using System.Web.UI;
using System.Web.UI.WebControls;

namespace WebApplication1
{
    public partial class WebForm1 : System.Web.UI.Page
    {
        protected void Page_Load(object sender, EventArgs e)
        {
            // mozna zastapic kontener Application poprzez uzycie zmiennych statycznych
            // ( tylko trzeba wtedy uwazac na wrazliwe odwolania, np. uzycie bazy danych)
            var service = (MyService)Application["MyServiceInstance"];
            ResultLabel.Text = service.DoWork();

            Session["SessionData"] = "This is session data!";

            Context.Items["RequestData"] = "Data only for this request.";

            Response.Write("Session Data: " + Session["SessionData"] + "<br>");

            Response.Write("Request Data: " + Context.Items["RequestData"] + "<br>");
        }
    }
}