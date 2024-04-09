package light;
public class Light {

    private boolean isOn;
    private int intensity;

    public Light() {
        this.isOn = false;
        this.intensity = 0;
    }

    public void turnOn() {
        this.isOn = true;
    }

    public void turnOff() {
        this.isOn = false;
    }

    public void setIntensity(int intensity) {
        this.intensity = intensity;
    }

    public boolean isOn() {
        return isOn;
    }

    public int getIntensity() {
        return intensity;
    }

}
