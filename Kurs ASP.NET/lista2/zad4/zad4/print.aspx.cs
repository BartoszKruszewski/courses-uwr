using System;
using System.Collections.Generic;
using System.Linq;
using System.Web;
using System.Web.UI;
using System.Web.UI.WebControls;

namespace zad4
{
    public partial class print : Page
    {
        protected void Page_Load(object sender, EventArgs e)
        {
            if (Session["Course"] == null)
            {
                Response.Redirect("start.aspx");
            }
        }
    }
}