<%@ page contentType="text/html;charset=UTF-8" language="java" %>
<%@ page import="java.util.List" %>
<%@ page import="Dao.User" %>
<html>
<head>
    <title>Dashboard</title>
</head>
<body>
<h2>Welcome, ${user.username}!</h2>
<h3>Registered Users:</h3>
<% List<User> userList = (List<User>) request.getAttribute("userList");
   if (userList != null) {
       for (User user : userList) {
%>
    <p><%= user.getFullname() %> (<%= user.getUsername() %>)</p>
<%
       }
   }
%>
</body>
</html>
