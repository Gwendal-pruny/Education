package lights;
public class Test {

    public static void main(String[] args) {

        LightControlPanel panel = new LightControlPanel();

        Light light1 = new Light();
        Light light2 = new Light();

        panel.addLight(light1);
        panel.addLight(light2);

        // Allume la lumière 1
        panel.executeCommand(new TurnOnLightCommand(light1));

        // Éteint la lumière 2
        panel.executeCommand(new TurnOffLightCommand(light2));

        // Règle l'intensité de la lumière 1 à 50%
        panel.executeCommand(new AdjustBrightnessCommand(light1, 50));

        // Annule la dernière commande
        panel.undo();

        // Allume toutes les lumières
        panel.turnOnAllLights();

        // Éteint toutes les lumières
        panel.turnOffAllLights();
    }

}
