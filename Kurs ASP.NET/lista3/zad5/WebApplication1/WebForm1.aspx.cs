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
            if (!IsPostBack)
            {
                LoadData();
            }
        }

        protected void Button1_Click(object sender, EventArgs e)
        {
            // wykorzystanie pseudosingletona z DataContextProvider
            var dataContext = DataContextProvider.GetDataContext(HttpContext.Current);

            var newEntity = new ExampleEntity
            {
                Name = TextBox1.Text
            };

            dataContext.Add(newEntity);
            TextBox1.Text = string.Empty;
            LoadData();
        }

        private void LoadData()
        {
            var dataContext = DataContextProvider.GetDataContext(HttpContext.Current);
            GridView1.DataSource = dataContext.Select(e => new { e.Name }).ToList();
            GridView1.DataBind();
        }
    }
}