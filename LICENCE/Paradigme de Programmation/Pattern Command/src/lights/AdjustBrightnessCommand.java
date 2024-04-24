package lights;
public class AdjustBrightnessCommand implements Command, UndoableCommand {

    private Light light;
    private int previousIntensity;

    public AdjustBrightnessCommand(Light light, int newIntensity) {
        this.light = light;
        this.previousIntensity = light.getIntensity();
    }

    @Override
    public void execute() {
        light.setIntensity(previousIntensity);
    }

    @Override
    public void undo() {
        light.setIntensity(previousIntensity);
    }

}
