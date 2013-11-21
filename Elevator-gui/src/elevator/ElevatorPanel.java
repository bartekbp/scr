/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package elevator;

import java.awt.Color;
import java.awt.Dimension;
import java.awt.Graphics;
import java.awt.Rectangle;
import java.awt.event.MouseEvent;
import java.awt.event.MouseListener;
import java.util.concurrent.atomic.AtomicBoolean;
import java.util.logging.Level;
import java.util.logging.Logger;
import javax.swing.JPanel;
import javax.swing.UIManager;

/**
 *
 * @author janiec
 */
public class ElevatorPanel extends JPanel {

    private static final int N = 4;
    private static final int MARGIN = 20;
    private int ELEVATOR_W;
    private int ELEVATOR_H;
    private int LEVEL_H;
    private int H;
    

    private static final Color BACKGROUND = UIManager.getColor("Panel.background");
    private static final Color WEIGHT_OK = new Color(30, 255, 30);
    private static final Color WEIGHT_ALARM = new Color(255, 10, 10);

    private int elevatorPosition;
    private boolean[] doorsOpen;
    private boolean isOverweight;
    
    private class MouseHandler implements MouseListener {

        @Override
        public void mouseClicked(MouseEvent e) {

            Rectangle r = new Rectangle(MARGIN + 1,
                    H - ELEVATOR_H - elevatorPosition + 1,
                    ELEVATOR_W - 1, ELEVATOR_H - 1);
            if (r.contains(e.getPoint())) {
                isOverweight = !isOverweight;
                EventHandler.weight(isOverweight);
                getParent().repaint();
            } else {
                for (int i = 0; i < N; ++i) {
                    r = new Rectangle(MARGIN + ELEVATOR_W, H - ELEVATOR_H - i * LEVEL_H + 1,
                            5, ELEVATOR_H);
                    if (r.contains(e.getPoint())) {
                        doorsOpen[i] = !doorsOpen[i];
                        EventHandler.doors(i, doorsOpen[i]);
                        getParent().repaint();
                        break;
                    }
                }
            }
        }

        @Override
        public void mousePressed(MouseEvent e) {
        }

        @Override
        public void mouseReleased(MouseEvent e) {
        }

        @Override
        public void mouseEntered(MouseEvent e) {

        }

        @Override
        public void mouseExited(MouseEvent e) {
        }
    }
    
    class MoveController extends Thread {
        private static final int MOVE_TIME = 3000;
        private static final int STEPS = 11;
        private static final int TIME = MOVE_TIME / STEPS;
        
        public AtomicBoolean working = new AtomicBoolean(true);
        private int startPos;
        private int endPos;

        public MoveController(int startPos, int endPos) {
            this.startPos = startPos;
            this.endPos = endPos;
        }
        
        

        @Override
        public void run() {
            int step = 0;
            while(working.get()) {
                if(++step == STEPS) {
                    setElevatorPosition(endPos);
                    break;
                } else {
                    setElevatorPosition(startPos + step * ((endPos - startPos) / STEPS));
                    try {
                        sleep(TIME);
                    } catch (InterruptedException ex) {
                        Logger.getLogger(ElevatorPanel.class.getName()).log(Level.SEVERE, null, ex);
                    }
                }
            }
            
        }        
    }
    
    private MoveController controller;

    public ElevatorPanel() {
        elevatorPosition = 0;
        doorsOpen = new boolean[N];
        isOverweight = false;
        repaint();
        addMouseListener(new MouseHandler());
    }

    private void setElevatorPosition(int elevatorPosition) {
        this.elevatorPosition = elevatorPosition;
        getParent().repaint();
    }
    
    public void startMove(int desiredLevel) {
        if(controller != null) {
            stopMove();
        }
        int end = desiredLevel * LEVEL_H;
        controller = new MoveController(elevatorPosition, end);
        controller.start();
    }
    
    public void stopMove(){
        if(controller != null) {
            controller.working.set(false);
            controller = null;
        }
    }    

    @Override
    protected void paintComponent(Graphics g) {
        super.paintComponent(g);
        Dimension d = getSize();
        LEVEL_H = (d.height - 2 * MARGIN) / N;
        ELEVATOR_H = LEVEL_H / 2;
        ELEVATOR_W = 2 * (d.width - 2 * MARGIN) / 3;
        H = MARGIN + N * LEVEL_H;
        g.setColor(Color.BLACK);
        for (int i = 0; i < N; ++i) {
            if (doorsOpen[i]) {
                g.drawLine(MARGIN + ELEVATOR_W, H - N * ELEVATOR_H,
                        MARGIN + 2 * ELEVATOR_W, H - N * ELEVATOR_H);
            }
        }
        g.drawRect(MARGIN, MARGIN, ELEVATOR_W, N * LEVEL_H);
        if (isOverweight) {
            g.setColor(WEIGHT_ALARM);
        } else {
            g.setColor(WEIGHT_OK);
        }
        g.fillRect(MARGIN + 1, H - ELEVATOR_H - elevatorPosition + 1,
                ELEVATOR_W - 1, ELEVATOR_H - 1);

        for (int i = 0; i < N; ++i) {
            g.setColor(WEIGHT_OK);
            if (doorsOpen[i]) {
                g.setColor(BACKGROUND);
            } else {
                g.setColor(Color.BLACK);
            }
            g.fillRect(MARGIN + ELEVATOR_W, H - ELEVATOR_H - i * LEVEL_H + 1,
                    3, ELEVATOR_H);
            if (i == 2) {
                g.setColor(BACKGROUND);
                g.fillRect(MARGIN + ELEVATOR_W+1,
                        H - ELEVATOR_H - i * LEVEL_H + 1 + ELEVATOR_H,
                        60, ELEVATOR_H);
            }
        }

    }

}
