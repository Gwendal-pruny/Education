package light;
import java.util.ArrayList;
import java.util.List;

public class LightControlPanel {

    private List<Command> executedCommands;
    private List<Light> lights;

    public LightControlPanel() {
        this.lights = new ArrayList<>();
        this.executedCommands = new ArrayList<>();
    }

    public void addLight(Light light) {
        this.lights.add(light);
    }

    public void removeLight(Light light) {
        this.lights.remove(light);
    }

    public void turnOnAllLights() {
        for (Light light : lights) {
            light.turnOn();
        }
    }

    public void turnOffAllLights() {
        for (Light light : lights) {
            light.turnOff();
        }
    }

    public void executeCommand(Command command) {
        command.execute();
        executedCommands.add(command);
    }

    public void undo() {
        if (executedCommands != null && !executedCommands.isEmpty()) {
            Command lastCommand = executedCommands.remove(executedCommands.size() - 1);
            if (lastCommand instanceof UndoableCommand) {
                ((UndoableCommand) lastCommand).undo();
            }
        }
    }

    public List<Light> getLights() {
        return lights; // Provide access to the light list
    }
    public interface LightChangeListener {
        void onLightAdded(Light light);
        void onLightRemoved(Light light);
    }

    private List<LightChangeListener> listeners = new ArrayList<>();

    public void addLightChangeListener(LightChangeListener listener) {
        listeners.add(listener);
    }

    protected void notifyLightAdded(Light light) {
        for (LightChangeListener listener : listeners) {
            listener.onLightAdded(light);
        }
    }

    protected void notifyLightRemoved(Light light) {
        for (LightChangeListener listener : listeners) {
            listener.onLightRemoved(light);
        }
    }
}
