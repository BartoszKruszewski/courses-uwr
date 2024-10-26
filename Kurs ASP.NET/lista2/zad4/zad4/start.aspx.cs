using System;
using System.Web;
using System.Web.UI;
using System.Web.UI.WebControls;

namespace zad4
{
    public partial class start : System.Web.UI.Page
    {
        protected void Page_Load(object sender, EventArgs e)
        {
            for (int i = 1; i <= 10; i++)
            {
                TextBox txtTask = new TextBox
                {
                    ID = $"txtTask{i}",
                    MaxLength = 2
                };
                TaskPanel.Controls.Add(new LiteralControl($"Zadanie {i}: "));
                TaskPanel.Controls.Add(txtTask);
                TaskPanel.Controls.Add(new LiteralControl("<br />"));
            }
        }

        protected void btnSubmit_Click(object sender, EventArgs e)
        {
            if (!Page.IsValid)
            {
                lblError.Text = "Proszę wprowadzić poprawne dane.";
                lblError.Visible = true;
                return;
            }

            Session["Name"] = txtName.Text;
            Session["Date"] = txtDate.Text;
            Session["Course"] = txtCourse.Text;
            Session["SetNumber"] = txtSetNumber.Text;

            for (int i = 1; i <= 10; i++)
            {
                TextBox txtTask = (TextBox)TaskPanel.FindControl($"txtTask{i}");
                Session[$"Task{i}"] = txtTask.Text;
            }

            string url = $"print.aspx?name={HttpUtility.UrlEncode(txtName.Text)}&date={HttpUtility.UrlEncode(txtDate.Text)}";
            Response.Redirect(url);
        }
    }
}