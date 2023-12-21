import javax.swing.*;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

public class SimpleCalculator extends JFrame {
    private JTextField display;
    private JPanel buttonPanel;
    private double result;
    private String operator;
    private boolean readyForNewInput;

    public SimpleCalculator() {
        setTitle("Simple Calculator");
        setSize(400, 500);
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        setLocationRelativeTo(null);
        display = new JTextField("0", 20);
        display.setEditable(false);
        display.setHorizontalAlignment(JTextField.RIGHT);
        display.setFont(new Font("Arial", Font.BOLD, 60));
        display.setBackground(Color.BLACK);
        display.setForeground(Color.WHITE);

        buttonPanel = new JPanel();
        buttonPanel.setLayout(new GridLayout(4, 4, 2, 2));

        String[] buttons = {
                "7", "8", "9", "/",
                "4", "5", "6", "*",
                "1", "2", "3", "-",
                "0", ".", "=", "+"
        };

        for (String text : buttons) {
            JButton button = new JButton(text);
            button.setFont(new Font("Arial", Font.BOLD, 30));
            button.setForeground(Color.DARK_GRAY);
            button.addActionListener(new ButtonClickListener());
            button.setFocusPainted(false);
            buttonPanel.add(button);
        }

        add(display, BorderLayout.NORTH);
        add(buttonPanel, BorderLayout.CENTER);
    }

    private class ButtonClickListener implements ActionListener {
        public void actionPerformed(ActionEvent e) {
            String input = e.getActionCommand();

            if ("0123456789.".contains(input)) {
                if (readyForNewInput || "0".equals(display.getText())) {
                    display.setText(input);
                    readyForNewInput = false;
                } else {
                    display.setText(display.getText() + input);
                }
            } else if ("+-*/".contains(input)) {
                operator = input;
                result = Double.parseDouble(display.getText());
                readyForNewInput = true;
            } else if ("=".equals(input)) {
                switch (operator) {
                    case "+":
                        result += Double.parseDouble(display.getText());
                        break;
                    case "-":
                        result -= Double.parseDouble(display.getText());
                        break;
                    case "*":
                        result *= Double.parseDouble(display.getText());
                        break;
                    case "/":
                        result /= Double.parseDouble(display.getText());
                        break;
                }
                display.setText(String.valueOf(result));
                readyForNewInput = true;
            }
        }
    }

    public static void main(String[] args) {
        SwingUtilities.invokeLater(new Runnable() {
            public void run() {
                try {
                    UIManager.setLookAndFeel("com.sun.java.swing.plaf.windows.WindowsLookAndFeel");
                } catch (Exception e) {
                    e.printStackTrace();
                }
                new SimpleCalculator().setVisible(true);
            }
        });
    }
}