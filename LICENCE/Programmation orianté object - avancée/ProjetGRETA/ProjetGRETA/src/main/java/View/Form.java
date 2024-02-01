package View;


import jakarta.servlet.ServletException;
import jakarta.servlet.annotation.WebServlet;
import jakarta.servlet.http.HttpServlet;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;

import java.io.*;

public class Form extends HttpServlet {

  public void doGet(HttpServletRequest request, HttpServletResponse response)
  throws ServletException, IOException {
      response.setContentType("text/html; charset=UTF-8");
      request.setCharacterEncoding("UTF-8");
      
      PrintWriter out = response.getWriter();
      try {
          String nom = request.getParameter("nom");
          String nbHeures = request.getParameter("nbHeures");

          out.println("<!DOCTYPE html>");
          out.println("<html lang='fr'>");
          out.println("<head>");
          out.println("<meta charset='UTF-8'>");
          out.println("<title>Résultat du formulaire</title>");
          out.println("</head>");
          out.println("<body>");
          out.println("<h1>Résultat du formulaire</h1>");
          out.println("<p>Nom : " + (nom != null ? nom : "") + "</p>");
          out.println("<p>Nombre d'heures : " + (nbHeures != null ? nbHeures : "") + "</p>");
          out.println("</body>");
          out.println("</html>");
      } finally {
          out.close();
      }
  }
}