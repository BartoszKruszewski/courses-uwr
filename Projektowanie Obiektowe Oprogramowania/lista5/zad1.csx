#r "System.Net.Mail"

using System.Net;
using System.Net.Mail;
using System.IO;

var smtp = new SmtpFacade();
smtp.Send("noreply@example.com", "recipient@example.com", "Test", "Test");
public class SmtpFacade
{
    public void Send(string from, string to, string subject, string body)
    {
        var mail = new MailMessage(from, to, subject, body);
        var smtp = new SmtpClient("smtp.example.com", 587);
        smtp.Credentials = new NetworkCredential("username", "password");
        smtp.EnableSsl = true;
        smtp.Send(mail);
    }
}
