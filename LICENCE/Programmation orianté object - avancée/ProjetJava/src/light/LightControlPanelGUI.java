package light;
import java.awt.BorderLayout;
import java.awt.Color;
import java.awt.GridLayout;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.awt.event.MouseAdapter;
import java.awt.event.MouseEvent;
import java.util.List;

import javax.swing.BorderFactory;
import javax.swing.ImageIcon;
import javax.swing.JButton;
import javax.swing.JFrame;
import javax.swing.JLabel;
import javax.swing.JPanel;
import javax.swing.JScrollPane;
import javax.swing.JSlider;
import javax.swing.event.ChangeEvent;
import javax.swing.event.ChangeListener;

public class LightControlPanelGUI extends JFrame implements ActionListener, ChangeListener {

    private LightControlPanel controlPanel;
    private List<Light> lights; // Reference to light list from control panel

    private JButton btnTurnOnAll, btnTurnOffAll, btnAddLight, btnRemoveLight;
    private JSlider sliderBrightness;
    private JLabel lblLightStatus;
    private ImageIcon lightOnIcon, lightOffIcon;
    private JLabel lblLight1Image, lblLight2Image;
    private JButton btnUndoLastAction; // Button to undo the last action
    private JLabel lblLight1Name, lblLight2Name; // Labels for light names with intensity
    private JPanel lightsPanel; // Panel pour afficher dynamiquement les lumières

    public enum ActionType {
        TURN_ON_ALL,
        TURN_OFF_ALL,
        ADD_LIGHT,
        REMOVE_LIGHT,
        NONE // Utilisé pour indiquer qu'aucune action précédente n'est à annuler
    }
    
    private ActionType lastActionType = ActionType.NONE;
    private Light lastModifiedLight = null; // Dernière lumière ajoutée ou supprimée

    public LightControlPanelGUI(LightControlPanel controlPanel) {
    	this.controlPanel = controlPanel;
        this.lights = controlPanel.getLights(); // Get the list of lights
        // Initialize GUI components
        initComponents();
        // Update light status display
        updateLightStatus();
    }

    private void initComponents() {
        // Initialize light icons
        try {
            lightOnIcon = new ImageIcon(getClass().getResource("/light_on.png"));
            lightOffIcon = new ImageIcon(getClass().getResource("/light_off.png"));
        } catch (Exception e) {
            lightOnIcon = new ImageIcon(); // Provide a default icon in case of failure
            lightOffIcon = new ImageIcon();
            System.err.println("Error: Image files not found! Ensure 'light_on.png' and 'light_off.png' are in the project directory.");
        }
        lblLightStatus = new JLabel("Light Status: Off"); // Ensure this line is before updateLightStatus() is called

        // Initialize light label images
        lblLight1Image = new JLabel(lightOffIcon);
        lblLight2Image = new JLabel(lightOffIcon);

        // Initialize the labels for light names with intensities
        lblLight1Name = new JLabel("Light 1: 0%");
        lblLight2Name = new JLabel("Light 2: 0%");

        // Initialisation du panel pour les lumières, avec une disposition flexible
        lightsPanel = new JPanel(new GridLayout(0, 4)); // Nombre de lignes variable, 4 colonnes

        // Slider for brightness
        sliderBrightness = new JSlider(0, 100, 50);
        sliderBrightness.setMajorTickSpacing(10);
        sliderBrightness.setMinorTickSpacing(1);
        sliderBrightness.setPaintTicks(true);
        sliderBrightness.setPaintLabels(true);
        sliderBrightness.addChangeListener(this);
        // Slider for brightness
        sliderBrightness = new JSlider(0, 100, 50);
        sliderBrightness.setMajorTickSpacing(10);
        sliderBrightness.setMinorTickSpacing(1);
        sliderBrightness.setPaintTicks(true);
        sliderBrightness.setPaintLabels(true);
        
        // Ajoutez le ChangeListener ici, dans initComponents()
        sliderBrightness.addChangeListener(new ChangeListener() {
            @Override
            public void stateChanged(ChangeEvent e) {
                if (selectedLight != null && !sliderBrightness.getValueIsAdjusting()) {
                    selectedLight.setIntensity(sliderBrightness.getValue());
                    updateLightStatus(); // Mettre à jour l'affichage pour refléter la nouvelle intensité
                }
            }
        });

        // Button panel for light control
        JPanel buttonPanel = new JPanel(new GridLayout(1, 5));
        btnTurnOnAll = new JButton("Turn All On");
        btnTurnOffAll = new JButton("Turn All Off");
        btnAddLight = new JButton("Add Light");
        btnRemoveLight = new JButton("Remove Light");
        btnUndoLastAction = new JButton("Undo Last Action");
        
        buttonPanel.add(btnTurnOnAll);
        buttonPanel.add(btnTurnOffAll);
        buttonPanel.add(btnAddLight);
        buttonPanel.add(btnRemoveLight);
        buttonPanel.add(btnUndoLastAction);
        

        JPanel mainPanel = new JPanel(new BorderLayout());
        mainPanel.add(buttonPanel, BorderLayout.NORTH);
        mainPanel.add(new JScrollPane(lightsPanel), BorderLayout.CENTER); // Utilisation d'un JScrollPane pour supporter le scrolling
        mainPanel.add(sliderBrightness, BorderLayout.SOUTH);


        // Add the main panel to the frame
        this.getContentPane().add(mainPanel);

        // Action listeners for buttons
        btnTurnOnAll.addActionListener(this);
        btnTurnOffAll.addActionListener(this);
        btnAddLight.addActionListener(this);
        btnRemoveLight.addActionListener(this);
        btnUndoLastAction.addActionListener(this);
    }

    @Override
    public void actionPerformed(ActionEvent e) {
        if (e.getSource() == btnTurnOnAll) {
            controlPanel.turnOnAllLights();
            lastActionType = ActionType.TURN_ON_ALL;
        } else if (e.getSource() == btnTurnOffAll) {
            controlPanel.turnOffAllLights();
            lastActionType = ActionType.TURN_OFF_ALL;
        } else if (e.getSource() == btnAddLight) {
            Light newLight = new Light();
            controlPanel.addLight(newLight);
            lastActionType = ActionType.ADD_LIGHT;
            lastModifiedLight = newLight; // Enregistre la lumière ajoutée
        } else if (e.getSource() == btnRemoveLight) {
            if (!lights.isEmpty()) {
                Light removedLight = lights.get(lights.size() - 1);
                controlPanel.removeLight(removedLight);
                lastActionType = ActionType.REMOVE_LIGHT;
                lastModifiedLight = removedLight; // Enregistre la lumière supprimée
            }
        } else if (e.getSource() == btnUndoLastAction) {
            undoLastAction();
        }
        lights = controlPanel.getLights();
        updateLightStatus();
    }

    private void undoLastAction() {
        switch (lastActionType) {
            case TURN_ON_ALL:
                controlPanel.turnOffAllLights();
                break;
            case TURN_OFF_ALL:
                controlPanel.turnOnAllLights();
                break;
            case ADD_LIGHT:
                if (lastModifiedLight != null) controlPanel.removeLight(lastModifiedLight);
                break;
            case REMOVE_LIGHT:
                if (lastModifiedLight != null) controlPanel.addLight(lastModifiedLight);
                break;
            default: // NONE ou tout autre cas
                // Pas d'action à annuler
                break;
        }
        lights = controlPanel.getLights(); // Mise à jour de la référence après annulation
        updateLightStatus(); // Mettre à jour l'affichage des lumières
        lastActionType = ActionType.NONE; // Réinitialise la dernière action
    }
    
    private Light selectedLight = null; // La lumière actuellement sélectionnée

    private void updateLightStatus() {
        lightsPanel.removeAll();

        for (Light light : lights) {
            JLabel lightLabel = new JLabel();
            lightLabel.setIcon(light.isOn() ? lightOnIcon : lightOffIcon);
            String lightText = "Light: " + (light.isOn() ? "On" : "Off") + " (" + light.getIntensity() + "%)";
            lightLabel.setText(lightText);

            JPanel lightPanel = new JPanel(new BorderLayout());
            lightPanel.add(lightLabel, BorderLayout.CENTER);
            
            // Définit la bordure en fonction de si la lumière est sélectionnée ou non
            if (selectedLight != null && selectedLight == light) {
                lightPanel.setBorder(BorderFactory.createLineBorder(Color.RED, 2)); // Lumière sélectionnée
            } else {
                lightPanel.setBorder(BorderFactory.createLineBorder(Color.BLACK)); // Autres lumières
            }
            
            lightPanel.addMouseListener(new MouseAdapter() {
                @Override
                public void mouseClicked(MouseEvent e) {
                    selectedLight = light;
                    sliderBrightness.setValue(light.getIntensity());
                    updateLightStatus(); // Mettre à jour l'affichage pour montrer la sélection
                }
            });

            lightsPanel.add(lightPanel);
        }

        lightsPanel.revalidate();
        lightsPanel.repaint();
    }



	@Override
	public void stateChanged(ChangeEvent e) {
		// TODO Auto-generated method stub
		
	}
}