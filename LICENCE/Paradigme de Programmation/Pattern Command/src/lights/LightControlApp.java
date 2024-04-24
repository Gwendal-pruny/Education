package lights;
public class LightControlApp {

    public static void main(String[] args) {

        // Create a LightControlPanel
        LightControlPanel controlPanel = new LightControlPanel();

        // Initialize some lights
        Light light1 = new Light();
        Light light2 = new Light();
        controlPanel.addLight(light1);
        controlPanel.addLight(light2);

        // Create a LightControlPanelGUI instance with the control panel
        LightControlPanelGUI gui = new LightControlPanelGUI(controlPanel);

        // Make the GUI frame visible
        gui.setVisible(true);
    }
}