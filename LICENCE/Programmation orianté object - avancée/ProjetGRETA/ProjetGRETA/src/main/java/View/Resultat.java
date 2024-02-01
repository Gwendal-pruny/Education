package View;

import jakarta.servlet.ServletException;
import jakarta.servlet.annotation.WebServlet;
import jakarta.servlet.http.HttpServlet;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import jakarta.servlet.http.HttpSession;

import java.io.IOException;
import java.io.PrintWriter;

import Model.Matiere;

@WebServlet("/Resultat")
public class Resultat extends HttpServlet {
    protected void doGet(HttpServletRequest request, HttpServletResponse response)
        throws ServletException, IOException {
        
        response.setContentType("text/html; charset=UTF-8");
        request.setCharacterEncoding("UTF-8");
        
        HttpSession session = request.getSession();
        Matiere matiere = (Matiere) session.getAttribute("matiere");
        
        String nom = matiere.getNom();
        String nbHeures = matiere.getNbHeures();
        
        
        PrintWriter out = response.getWriter();
        try {
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

