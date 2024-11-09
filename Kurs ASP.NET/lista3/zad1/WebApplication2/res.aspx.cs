using System;
using System.Collections.Generic;
using System.Linq;
using System.Web;
using System.Web.UI;
using System.Web.UI.WebControls;

namespace WebApplication2
{
    public partial class res : System.Web.UI.Page
    {
        protected void Page_Load(object sender, EventArgs e)
        {
            string param1 = Request["p1"];
            string param2 = Request["p2"];

            LabelP1.Text = param1 ?? "Brak danych";
            LabelP2.Text = param2 ?? "Brak danych";
        }
    }
}