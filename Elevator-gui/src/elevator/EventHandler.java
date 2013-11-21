/*
 * To change this template, choose Tools | Templates
 * and open the template in the editor.
 */
package elevator;

/**
 *
 * @author bartek
 */
import Default.*;
import static elevator.ElevatorGui.gen;
        
public class EventHandler {
    public static void bringHere(int a) { 
       gen(new BringHere(a));
    }
    public static void emergencyBringHere() {
        gen(new EmergencyBringHere());
    }
    public static void emergencyReady() {
        gen(new EmergencyReady());
    }
    public static void move(int a, int b) {
        gen(new Move(a,b));
    }
    public static void ready(int a) { 
        gen(new Ready(a));
    }
    public static void stop() {
        gen(new Stop());
    }
    
    public static void doors(int level, boolean areOpen) {
        gen(new DoorsOpened(level, areOpen));
    }
    
    public static void weight(boolean isOverweight) {
        gen(new OverLoaded(isOverweight));
    }
    
}
