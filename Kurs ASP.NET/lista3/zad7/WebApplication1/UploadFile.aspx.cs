using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using System.Text;
using System.Web;
using System.Web.UI;
using System.Web.UI.WebControls;

namespace WebApplication1
{
    public partial class UploadFile : System.Web.UI.Page
    {
        protected void btnUpload_Click(object sender, EventArgs e)
        {
            if (fileUpload.HasFile)
            {
                var fileName = Path.GetFileName(fileUpload.FileName);
                var fileSize = fileUpload.FileContent.Length;

                var fileBytes = new byte[fileSize];
                fileUpload.FileContent.Read(fileBytes, 0, (int)fileSize);
                var checksum = fileBytes.Sum(b => b) % 0xFFFF;

                var responseContent = new StringBuilder();
                responseContent.AppendLine("<opis>");
                responseContent.AppendLine($"<nazwa>{fileName}</nazwa>");
                responseContent.AppendLine($"<rozmiar>{fileSize}</rozmiar>");
                responseContent.AppendLine($"<sygnatura>{checksum}</sygnatura>");
                responseContent.AppendLine("</opis>");

                Response.Clear();
                Response.ContentType = "application/xml";

                string encodedFileName = Uri.EscapeDataString(fileName);
                Response.AddHeader("Content-Disposition", $"attachment; filename=\"{fileName}\"; filename*=UTF-8''{encodedFileName}");

                //Wersja bez UTF-8
                //Response.AddHeader("Content-Disposition", $"attachment; filename=\"file_info.xml\"");

                Response.Write(responseContent.ToString());
                Response.End();
            }
            else
            {
                Response.Write("Nie wybrano pliku.");
            }
        }
    }
}