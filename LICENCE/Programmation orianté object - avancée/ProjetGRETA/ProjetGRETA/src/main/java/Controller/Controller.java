package Controller;


import jakarta.servlet.ServletException;
import jakarta.servlet.annotation.WebServlet;
import jakarta.servlet.http.HttpServlet;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import jakarta.servlet.http.HttpSession;

import java.io.IOException;

import Model.Matiere;

@WebServlet("/Controller")
public class Controller extends HttpServlet {
    protected void doGet(HttpServletRequest request, HttpServletResponse response)
        throws ServletException, IOException {

        String nom = request.getParameter("nom");
//        String nbHeures = request.getParameter("nbHeures");

        	
    	Matiere matiere = new Matiere();
    	matiere.setNom(request.getParameter("nom"));
    	matiere.setNbHeures(request.getParameter("nbHeures"));
    	
        HttpSession session = request.getSession();
        session.setAttribute("matiere", matiere);
        
        if ("Math".equals(nom)) {
            response.sendRedirect("Final");
        } else {
            response.sendRedirect("Resultat");
        }
    }
}
