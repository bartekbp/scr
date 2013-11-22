/*********************************************************************
	Rhapsody	: 8.0.3
	Login		: janiec
	Component	: exe
	Configuration 	: DefaultConfig
	Model Element	: Elevator
//!	Generated Date	: Fri, 22, Nov 2013 
	File Path	: exe/DefaultConfig/Default/Elevator.java
*********************************************************************/

package Default;

//## auto_generated
import java.util.*;
//## auto_generated
import com.ibm.rational.rhapsody.oxf.*;
//## auto_generated
import com.ibm.rational.rhapsody.oxf.states.*;

//----------------------------------------------------------------------------
// Default/Elevator.java                                                                  
//----------------------------------------------------------------------------

//## package Default 


//## class Elevator 
public class Elevator implements RiJStateConcept {
    
    public Reactive reactive;		//## ignore 
    
    protected Elevator.ElevatorsEffectors effectors;		//## attribute effectors 
    
    protected boolean moving;		//## attribute moving 
    
    protected java.util.Vector requests;		//## attribute requests 
    
    protected BringHereHandler bh;		//## classInstance bh 
    
    protected DoorsController dc;		//## classInstance dc 
    
    protected DoorsOpenedHandler dh;		//## classInstance dh 
    
    protected ArrayList<Floor> fl;		//## classInstance fl 
    
    protected HeightController hc;		//## classInstance hc 
    
    protected LoadController lc;		//## classInstance lc 
    
    protected LoadHandler lh;		//## classInstance lh 
    
    protected MoveController mc;		//## classInstance mc 
    
    protected MoveHandler mh;		//## classInstance mh 
    
    protected ReadyController rc;		//## classInstance rc 
    
    protected ReadyHandler rh;		//## classInstance rh 
    
    //#[ ignore 
    public static final int RiJNonState=0;
    public static final int WorkingElevator=1;
    public static final int waitingForRequest=2;
    public static final int Stopped=3;
    public static final int Moving=4;
    public static final int Finished=5;
    public static final int EmergencyStopped=6;
    public static final int EmergencyMoving=7;
    public static final int EmergencyBaseLevel=8;
    //#]
    protected int rootState_subState;		//## ignore 
    
    protected int rootState_active;		//## ignore 
    
    protected int WorkingElevator_subState;		//## ignore 
    
    protected int WorkingElevator_lastState;		//## ignore 
    
    
    //## statechart_method 
    public RiJThread getThread() {
        return reactive.getThread();
    }
    
    //## statechart_method 
    public void schedTimeout(long delay, long tmID, RiJStateReactive reactive) {
        getThread().schedTimeout(delay, tmID, reactive);
    }
    
    //## statechart_method 
    public void unschedTimeout(long tmID, RiJStateReactive reactive) {
        getThread().unschedTimeout(tmID, reactive);
    }
    
    //## statechart_method 
    public boolean isIn(int state) {
        return reactive.isIn(state);
    }
    
    //## statechart_method 
    public boolean isCompleted(int state) {
        return reactive.isCompleted(state);
    }
    
    //## statechart_method 
    public RiJEventConsumer getEventConsumer() {
        return (RiJEventConsumer)reactive;
    }
    
    //## statechart_method 
    public void gen(RiJEvent event) {
        reactive._gen(event);
    }
    
    //## statechart_method 
    public void queueEvent(RiJEvent event) {
        reactive.queueEvent(event);
    }
    
    //## statechart_method 
    public int takeEvent(RiJEvent event) {
        return reactive.takeEvent(event);
    }
    
    // Constructors
    
    //## auto_generated 
    public  Elevator(RiJThread p_thread) {
        reactive = new Reactive(p_thread);
        fl = new ArrayList<Floor>();
        initRelations(p_thread);
    }
    
    /**
     * @param level
     * @param areOpen
    */
    //## operation GenDoorsOpen(int,boolean) 
    public void GenDoorsOpen(int level, boolean areOpen) {
        //#[ operation GenDoorsOpen(int,boolean) 
        dc.gen(new DoorsOpened(level,areOpen));
        //#]
    }
    
    /**
     * @param level
     * @param origin
    */
    //## operation GenMove(int,int) 
    public void GenMove(int level, int origin) {
        //#[ operation GenMove(int,int) 
        if(effectors != null) {
        	effectors.debugMessage("Sending Move");
        }
        mc.gen(new Move(level,origin));
        //#]
    }
    
    /**
     * @param isOverloaded
    */
    //## operation GenOverload(boolean) 
    public void GenOverload(boolean isOverloaded) {
        //#[ operation GenOverload(boolean) 
        lc.gen(new OverLoaded(isOverloaded));     
        if(effectors!=null) {
        	effectors.debugMessage("gen overload " + isOverloaded);
        }
        //#]
    }
    
    /**
     * @param level
    */
    //## operation GenReady(int) 
    public void GenReady(int level) {
        //#[ operation GenReady(int) 
        if(effectors!=null) {
        	effectors.debugMessage("genReady entered");
        }
        rc.gen(new Ready(level));
        //#]
    }
    
    //## auto_generated 
    public Elevator.ElevatorsEffectors getEffectors() {
        return effectors;
    }
    
    //## auto_generated 
    public void setEffectors(Elevator.ElevatorsEffectors p_effectors) {
        effectors = p_effectors;
    }
    
    //## auto_generated 
    public boolean getMoving() {
        return moving;
    }
    
    //## auto_generated 
    public void setMoving(boolean p_moving) {
        moving = p_moving;
    }
    
    //## auto_generated 
    public java.util.Vector getRequests() {
        return requests;
    }
    
    //## auto_generated 
    public void setRequests(java.util.Vector p_requests) {
        requests = p_requests;
    }
    
    //## auto_generated 
    public BringHereHandler getBh() {
        return bh;
    }
    
    //## auto_generated 
    public void __setBh(BringHereHandler p_BringHereHandler) {
        bh = p_BringHereHandler;
    }
    
    //## auto_generated 
    public void _setBh(BringHereHandler p_BringHereHandler) {
        if(bh != null)
            {
                bh.__setEl(null);
            }
        __setBh(p_BringHereHandler);
    }
    
    //## auto_generated 
    public BringHereHandler newBh(RiJThread p_thread) {
        bh = new BringHereHandler(p_thread);
        bh._setEl(this);
        return bh;
    }
    
    //## auto_generated 
    public void deleteBh() {
        bh.__setEl(null);
        bh=null;
    }
    
    //## auto_generated 
    public DoorsController getDc() {
        return dc;
    }
    
    //## auto_generated 
    public void __setDc(DoorsController p_DoorsController) {
        dc = p_DoorsController;
    }
    
    //## auto_generated 
    public void _setDc(DoorsController p_DoorsController) {
        if(dc != null)
            {
                dc.__setEl(null);
            }
        __setDc(p_DoorsController);
    }
    
    //## auto_generated 
    public DoorsController newDc(RiJThread p_thread) {
        dc = new DoorsController(p_thread);
        dc._setEl(this);
        return dc;
    }
    
    //## auto_generated 
    public void deleteDc() {
        dc.__setEl(null);
        dc=null;
    }
    
    //## auto_generated 
    public DoorsOpenedHandler getDh() {
        return dh;
    }
    
    //## auto_generated 
    public void __setDh(DoorsOpenedHandler p_DoorsOpenedHandler) {
        dh = p_DoorsOpenedHandler;
    }
    
    //## auto_generated 
    public void _setDh(DoorsOpenedHandler p_DoorsOpenedHandler) {
        if(dh != null)
            {
                dh.__setEl(null);
            }
        __setDh(p_DoorsOpenedHandler);
    }
    
    //## auto_generated 
    public DoorsOpenedHandler newDh(RiJThread p_thread) {
        dh = new DoorsOpenedHandler(p_thread);
        dh._setEl(this);
        return dh;
    }
    
    //## auto_generated 
    public void deleteDh() {
        dh.__setEl(null);
        dh=null;
    }
    
    //## auto_generated 
    public ListIterator<Floor> getFl() {
        ListIterator<Floor> iter = fl.listIterator();
        return iter;
    }
    
    //## auto_generated 
    public void _addFl(Floor p_Floor) {
        fl.add(p_Floor);
    }
    
    //## auto_generated 
    public Floor newFl() {
        Floor newFloor = new Floor();
        newFloor._setEl(this);
        fl.add(newFloor);
        return newFloor;
    }
    
    //## auto_generated 
    public void _removeFl(Floor p_Floor) {
        fl.remove(p_Floor);
    }
    
    //## auto_generated 
    public void deleteFl(Floor p_Floor) {
        p_Floor._setEl(null);
        fl.remove(p_Floor);
        p_Floor=null;
    }
    
    //## auto_generated 
    public HeightController getHc() {
        return hc;
    }
    
    //## auto_generated 
    public void __setHc(HeightController p_HeightController) {
        hc = p_HeightController;
    }
    
    //## auto_generated 
    public void _setHc(HeightController p_HeightController) {
        if(hc != null)
            {
                hc.__setEl(null);
            }
        __setHc(p_HeightController);
    }
    
    //## auto_generated 
    public HeightController newHc(RiJThread p_thread) {
        hc = new HeightController(p_thread);
        hc._setEl(this);
        return hc;
    }
    
    //## auto_generated 
    public void deleteHc() {
        hc.__setEl(null);
        hc=null;
    }
    
    //## auto_generated 
    public LoadController getLc() {
        return lc;
    }
    
    //## auto_generated 
    public void __setLc(LoadController p_LoadController) {
        lc = p_LoadController;
    }
    
    //## auto_generated 
    public void _setLc(LoadController p_LoadController) {
        if(lc != null)
            {
                lc.__setEl(null);
            }
        __setLc(p_LoadController);
    }
    
    //## auto_generated 
    public LoadController newLc(RiJThread p_thread) {
        lc = new LoadController(p_thread);
        lc._setEl(this);
        return lc;
    }
    
    //## auto_generated 
    public void deleteLc() {
        lc.__setEl(null);
        lc=null;
    }
    
    //## auto_generated 
    public LoadHandler getLh() {
        return lh;
    }
    
    //## auto_generated 
    public void __setLh(LoadHandler p_LoadHandler) {
        lh = p_LoadHandler;
    }
    
    //## auto_generated 
    public void _setLh(LoadHandler p_LoadHandler) {
        if(lh != null)
            {
                lh.__setEl(null);
            }
        __setLh(p_LoadHandler);
    }
    
    //## auto_generated 
    public LoadHandler newLh(RiJThread p_thread) {
        lh = new LoadHandler(p_thread);
        lh._setEl(this);
        return lh;
    }
    
    //## auto_generated 
    public void deleteLh() {
        lh.__setEl(null);
        lh=null;
    }
    
    //## auto_generated 
    public MoveController getMc() {
        return mc;
    }
    
    //## auto_generated 
    public void __setMc(MoveController p_MoveController) {
        mc = p_MoveController;
    }
    
    //## auto_generated 
    public void _setMc(MoveController p_MoveController) {
        if(mc != null)
            {
                mc.__setEl(null);
            }
        __setMc(p_MoveController);
    }
    
    //## auto_generated 
    public MoveController newMc(RiJThread p_thread) {
        mc = new MoveController(p_thread);
        mc._setEl(this);
        return mc;
    }
    
    //## auto_generated 
    public void deleteMc() {
        mc.__setEl(null);
        mc=null;
    }
    
    //## auto_generated 
    public MoveHandler getMh() {
        return mh;
    }
    
    //## auto_generated 
    public void __setMh(MoveHandler p_MoveHandler) {
        mh = p_MoveHandler;
    }
    
    //## auto_generated 
    public void _setMh(MoveHandler p_MoveHandler) {
        if(mh != null)
            {
                mh.__setEl(null);
            }
        __setMh(p_MoveHandler);
    }
    
    //## auto_generated 
    public MoveHandler newMh(RiJThread p_thread) {
        mh = new MoveHandler(p_thread);
        mh._setEl(this);
        return mh;
    }
    
    //## auto_generated 
    public void deleteMh() {
        mh.__setEl(null);
        mh=null;
    }
    
    //## auto_generated 
    public ReadyController getRc() {
        return rc;
    }
    
    //## auto_generated 
    public void __setRc(ReadyController p_ReadyController) {
        rc = p_ReadyController;
    }
    
    //## auto_generated 
    public void _setRc(ReadyController p_ReadyController) {
        if(rc != null)
            {
                rc.__setEl(null);
            }
        __setRc(p_ReadyController);
    }
    
    //## auto_generated 
    public ReadyController newRc(RiJThread p_thread) {
        rc = new ReadyController(p_thread);
        rc._setEl(this);
        return rc;
    }
    
    //## auto_generated 
    public void deleteRc() {
        rc.__setEl(null);
        rc=null;
    }
    
    //## auto_generated 
    public ReadyHandler getRh() {
        return rh;
    }
    
    //## auto_generated 
    public void __setRh(ReadyHandler p_ReadyHandler) {
        rh = p_ReadyHandler;
    }
    
    //## auto_generated 
    public void _setRh(ReadyHandler p_ReadyHandler) {
        if(rh != null)
            {
                rh.__setEl(null);
            }
        __setRh(p_ReadyHandler);
    }
    
    //## auto_generated 
    public ReadyHandler newRh(RiJThread p_thread) {
        rh = new ReadyHandler(p_thread);
        rh._setEl(this);
        return rh;
    }
    
    //## auto_generated 
    public void deleteRh() {
        rh.__setEl(null);
        rh=null;
    }
    
    //## auto_generated 
    protected void initRelations(RiJThread p_thread) {
        bh = newBh(p_thread);
        dc = newDc(p_thread);
        dh = newDh(p_thread);
        {
            for (int i = 0; i < 4; i++) 
                newFl();
            
        }
        hc = newHc(p_thread);
        lc = newLc(p_thread);
        lh = newLh(p_thread);
        mc = newMc(p_thread);
        mh = newMh(p_thread);
        rc = newRc(p_thread);
        rh = newRh(p_thread);
    }
    
    //## auto_generated 
    public boolean startBehavior() {
        boolean done = true;
        done &= bh.startBehavior();
        done &= dc.startBehavior();
        done &= dh.startBehavior();
        done &= hc.startBehavior();
        done &= lc.startBehavior();
        done &= lh.startBehavior();
        done &= mc.startBehavior();
        done &= mh.startBehavior();
        done &= rc.startBehavior();
        done &= rh.startBehavior();
        done &= reactive.startBehavior();
        return done;
    }
    
    //## ignore 
    public class Reactive extends RiJStateReactive {
        
        // Default constructor 
        public Reactive() {
            this(RiJMainThread.instance());
        }
        
        
        // Constructors
        
        public  Reactive(RiJThread p_thread) {
            super(p_thread);
            initStatechart();
        }
        
        //## statechart_method 
        public boolean isIn(int state) {
            if(WorkingElevator_subState == state)
                {
                    return true;
                }
            if(rootState_subState == state)
                {
                    return true;
                }
            return false;
        }
        
        //## statechart_method 
        public boolean isCompleted(int state) {
            return true;
        }
        
        //## statechart_method 
        public void rootState_entDef() {
            {
                rootState_enter();
                rootStateEntDef();
            }
        }
        
        //## statechart_method 
        public int rootState_dispatchEvent(short id) {
            int res = RiJStateReactive.TAKE_EVENT_NOT_CONSUMED;
            switch (rootState_active) {
                case EmergencyStopped:
                {
                    res = EmergencyStopped_takeEvent(id);
                }
                break;
                case EmergencyMoving:
                {
                    res = EmergencyMoving_takeEvent(id);
                }
                break;
                case EmergencyBaseLevel:
                {
                    res = EmergencyBaseLevel_takeEvent(id);
                }
                break;
                case Stopped:
                {
                    res = Stopped_takeEvent(id);
                }
                break;
                case waitingForRequest:
                {
                    res = waitingForRequest_takeEvent(id);
                }
                break;
                case Finished:
                {
                    res = Finished_takeEvent(id);
                }
                break;
                case Moving:
                {
                    res = Moving_takeEvent(id);
                }
                break;
                default:
                    break;
            }
            return res;
        }
        
        //## auto_generated 
        protected void initStatechart() {
            rootState_subState = RiJNonState;
            rootState_active = RiJNonState;
            WorkingElevator_subState = RiJNonState;
            WorkingElevator_lastState = RiJNonState;
        }
        
        //## statechart_method 
        public int FinishedTakeNull() {
            int res = RiJStateReactive.TAKE_EVENT_NOT_CONSUMED;
            //## transition 6 
            if(requests.size() != 0)
                {
                    Finished_exit();
                    Moving_entDef();
                    res = RiJStateReactive.TAKE_EVENT_COMPLETE;
                }
            else
                {
                    //## transition 7 
                    if(requests.size() == 0)
                        {
                            Finished_exit();
                            waitingForRequest_entDef();
                            res = RiJStateReactive.TAKE_EVENT_COMPLETE;
                        }
                }
            return res;
        }
        
        //## statechart_method 
        public void Moving_enter() {
            WorkingElevator_subState = Moving;
            rootState_active = Moving;
            MovingEnter();
        }
        
        //## statechart_method 
        public int waitingForRequest_takeEvent(short id) {
            int res = RiJStateReactive.TAKE_EVENT_NOT_CONSUMED;
            if(event.isTypeOf(BringHere.BringHere_Default_id))
                {
                    res = waitingForRequestTakeBringHere();
                }
            
            if(res == RiJStateReactive.TAKE_EVENT_NOT_CONSUMED)
                {
                    res = WorkingElevator_takeEvent(id);
                }
            return res;
        }
        
        //## statechart_method 
        public void EmergencyBaseLevelEnter() {
        }
        
        //## statechart_method 
        public void EmergencyMoving_entDef() {
            EmergencyMoving_enter();
        }
        
        //## statechart_method 
        public int StoppedTakeMoveControllerE() {
            MoveControllerE params = (MoveControllerE) event;
            int res = RiJStateReactive.TAKE_EVENT_NOT_CONSUMED;
            //## transition 13 
            if(!(lc.isOverloaded || fl.get(0).areDoorsOpened || fl.get(1).areDoorsOpened || fl.get(2).areDoorsOpened || fl.get(3).areDoorsOpened ))
                {
                    Stopped_exit();
                    //#[ transition 13 
                    requests.add(0, params.level);
                    //#]
                    Moving_entDef();
                    res = RiJStateReactive.TAKE_EVENT_COMPLETE;
                }
            return res;
        }
        
        //## statechart_method 
        public void StoppedEnter() {
            //#[ state ROOT.WorkingElevator.Stopped.(Entry) 
            moving = false;
            if(effectors != null) {
            	effectors.debugMessage("Stopped entered");
            }
            //#]
        }
        
        //## statechart_method 
        public void waitingForRequestEnter() {
            //#[ state ROOT.WorkingElevator.waitingForRequest.(Entry) 
            if(effectors != null) {
            	effectors.debugMessage("WaitingForRequest entered");
            }
            //#]
        }
        
        //## statechart_method 
        public void waitingForRequest_entDef() {
            waitingForRequest_enter();
        }
        
        //## statechart_method 
        public int EmergencyStopped_takeEvent(short id) {
            int res = RiJStateReactive.TAKE_EVENT_NOT_CONSUMED;
            if(event.isTypeOf(EmergencyBringHere.EmergencyBringHere_Default_id))
                {
                    res = EmergencyStoppedTakeEmergencyBringHere();
                }
            else if(event.isTypeOf(EmergencyReady.EmergencyReady_Default_id))
                {
                    res = EmergencyStoppedTakeEmergencyReady();
                }
            
            if(res == RiJStateReactive.TAKE_EVENT_NOT_CONSUMED)
                {
                    res = WorkingElevator_takeEvent(id);
                }
            return res;
        }
        
        //## statechart_method 
        public void WorkingElevator_entHist() {
            WorkingElevatorEntHist();
        }
        
        //## statechart_method 
        public void EmergencyBaseLevel_exit() {
            EmergencyBaseLevelExit();
        }
        
        //## statechart_method 
        public int MovingTakeLevelController() {
            int res = RiJStateReactive.TAKE_EVENT_NOT_CONSUMED;
            Moving_exit();
            Stopped_entDef();
            res = RiJStateReactive.TAKE_EVENT_COMPLETE;
            return res;
        }
        
        //## statechart_method 
        public void Stopped_exit() {
            StoppedExit();
        }
        
        //## statechart_method 
        public void waitingForRequest_exit() {
            waitingForRequestExit();
        }
        
        //## statechart_method 
        public void EmergencyBaseLevel_enter() {
            WorkingElevator_subState = EmergencyBaseLevel;
            rootState_active = EmergencyBaseLevel;
            EmergencyBaseLevelEnter();
        }
        
        //## statechart_method 
        public void EmergencyStopped_entDef() {
            EmergencyStopped_enter();
        }
        
        //## statechart_method 
        public void Stopped_enter() {
            WorkingElevator_subState = Stopped;
            rootState_active = Stopped;
            StoppedEnter();
        }
        
        //## statechart_method 
        public void Stopped_entDef() {
            Stopped_enter();
        }
        
        //## statechart_method 
        public int waitingForRequestTakeBringHere() {
            BringHere params = (BringHere) event;
            int res = RiJStateReactive.TAKE_EVENT_NOT_CONSUMED;
            //## transition 5 
            if(!(lc.isOverloaded || fl.get(0).areDoorsOpened || fl.get(1).areDoorsOpened || fl.get(2).areDoorsOpened || fl.get(3).areDoorsOpened ))
                {
                    waitingForRequest_exit();
                    //#[ transition 5 
                    requests.add(params.level);
                    //#]
                    Moving_entDef();
                    res = RiJStateReactive.TAKE_EVENT_COMPLETE;
                }
            return res;
        }
        
        //## statechart_method 
        public void WorkingElevatorEntHist() {
            if(WorkingElevator_lastState == RiJNonState)
                {
                    EmergencyStopped_entDef();
                }
            else
                {
                    WorkingElevator_subState = WorkingElevator_lastState;
                    switch (WorkingElevator_subState) {
                        case EmergencyStopped:
                        {
                            EmergencyStopped_enter();
                        }
                        break;
                        case EmergencyMoving:
                        {
                            EmergencyMoving_enter();
                        }
                        break;
                        case EmergencyBaseLevel:
                        {
                            EmergencyBaseLevel_enter();
                        }
                        break;
                        case Stopped:
                        {
                            Stopped_enter();
                        }
                        break;
                        case waitingForRequest:
                        {
                            waitingForRequest_enter();
                        }
                        break;
                        case Finished:
                        {
                            Finished_enter();
                        }
                        break;
                        case Moving:
                        {
                            Moving_enter();
                        }
                        break;
                        default:
                            break;
                    }
                }
        }
        
        //## statechart_method 
        public void EmergencyBaseLevel_entDef() {
            EmergencyBaseLevel_enter();
        }
        
        //## statechart_method 
        public int Finished_takeEvent(short id) {
            int res = RiJStateReactive.TAKE_EVENT_NOT_CONSUMED;
            if(event.isTypeOf(RiJEvent.NULL_EVENT_ID))
                {
                    res = FinishedTakeNull();
                }
            else if(event.isTypeOf(DoorsOpenedController.DoorsOpenedController_Default_id))
                {
                    res = FinishedTakeDoorsOpenedController();
                }
            
            if(res == RiJStateReactive.TAKE_EVENT_NOT_CONSUMED)
                {
                    res = WorkingElevator_takeEvent(id);
                }
            return res;
        }
        
        //## statechart_method 
        public int StoppedTakeDoorsOpenedController() {
            DoorsOpenedController params = (DoorsOpenedController) event;
            int res = RiJStateReactive.TAKE_EVENT_NOT_CONSUMED;
            //#[ transition 10 
             fl.get(hc.getLevel()).areDoorsOpened = params.areOpened;
            //#]
            res = RiJStateReactive.TAKE_EVENT_COMPLETE;
            return res;
        }
        
        //## statechart_method 
        public int WorkingElevator_takeEvent(short id) {
            int res = RiJStateReactive.TAKE_EVENT_NOT_CONSUMED;
            if(event.isTypeOf(Stop.Stop_Default_id))
                {
                    res = WorkingElevatorTakeStop();
                }
            else if(event.isTypeOf(BringHere.BringHere_Default_id))
                {
                    res = WorkingElevatorTakeBringHere();
                }
            else if(event.isTypeOf(DoorsOpened.DoorsOpened_Default_id))
                {
                    res = WorkingElevatorTakeDoorsOpened();
                }
            
            return res;
        }
        
        //## statechart_method 
        public int WorkingElevatorTakeStop() {
            int res = RiJStateReactive.TAKE_EVENT_NOT_CONSUMED;
            WorkingElevator_exit();
            //#[ transition 11 
            hc.gen(new Stop());
            //#]
            WorkingElevator_enter();
            EmergencyStopped_entDef();
            res = RiJStateReactive.TAKE_EVENT_COMPLETE;
            return res;
        }
        
        //## statechart_method 
        public int rootState_takeEvent(short id) {
            int res = RiJStateReactive.TAKE_EVENT_NOT_CONSUMED;
            return res;
        }
        
        //## statechart_method 
        public int EmergencyStoppedTakeEmergencyBringHere() {
            int res = RiJStateReactive.TAKE_EVENT_NOT_CONSUMED;
            EmergencyStopped_exit();
            EmergencyMoving_entDef();
            res = RiJStateReactive.TAKE_EVENT_COMPLETE;
            return res;
        }
        
        //## statechart_method 
        public void FinishedEnter() {
            //#[ state ROOT.WorkingElevator.Finished.(Entry) 
            if(effectors != null) {
            	effectors.debugMessage("Finished entered");
            }
            //#]
        }
        
        //## statechart_method 
        public void waitingForRequestExit() {
        }
        
        //## statechart_method 
        public void WorkingElevatorExit() {
        }
        
        //## statechart_method 
        public int Moving_takeEvent(short id) {
            int res = RiJStateReactive.TAKE_EVENT_NOT_CONSUMED;
            if(event.isTypeOf(LevelController.LevelController_Default_id))
                {
                    res = MovingTakeLevelController();
                }
            
            if(res == RiJStateReactive.TAKE_EVENT_NOT_CONSUMED)
                {
                    res = WorkingElevator_takeEvent(id);
                }
            return res;
        }
        
        //## statechart_method 
        public void rootState_enter() {
            rootStateEnter();
        }
        
        //## statechart_method 
        public void rootStateEnter() {
        }
        
        //## statechart_method 
        public int FinishedTakeDoorsOpenedController() {
            DoorsOpenedController params = (DoorsOpenedController) event;
            int res = RiJStateReactive.TAKE_EVENT_NOT_CONSUMED;
            Finished_exit();
            //#[ transition 9 
            fl.get(hc.getLevel()).areDoorsOpened = true;
            //#]
            Stopped_entDef();
            res = RiJStateReactive.TAKE_EVENT_COMPLETE;
            return res;
        }
        
        //## statechart_method 
        public int EmergencyBaseLevelTakeEmergencyReady() {
            int res = RiJStateReactive.TAKE_EVENT_NOT_CONSUMED;
            EmergencyBaseLevel_exit();
            Stopped_entDef();
            res = RiJStateReactive.TAKE_EVENT_COMPLETE;
            return res;
        }
        
        //## statechart_method 
        public void EmergencyMoving_enter() {
            WorkingElevator_subState = EmergencyMoving;
            rootState_active = EmergencyMoving;
            EmergencyMovingEnter();
        }
        
        //## statechart_method 
        public void EmergencyMovingEnter() {
            //#[ state ROOT.WorkingElevator.EmergencyMoving.(Entry) 
            moving = true;
            hc.gen(new MoveControllerE(0));  
            if(effectors != null) {
            	effectors.debugMessage("EmergencyMoving entered");
            }
            //#]
        }
        
        //## statechart_method 
        public void EmergencyStoppedExit() {
        }
        
        //## statechart_method 
        public void EmergencyStopped_enter() {
            WorkingElevator_subState = EmergencyStopped;
            rootState_active = EmergencyStopped;
            EmergencyStoppedEnter();
        }
        
        //## statechart_method 
        public void Finished_exit() {
            popNullConfig();
            FinishedExit();
        }
        
        //## statechart_method 
        public void FinishedExit() {
        }
        
        //## statechart_method 
        public void Finished_enter() {
            pushNullConfig();
            WorkingElevator_subState = Finished;
            rootState_active = Finished;
            FinishedEnter();
        }
        
        //## statechart_method 
        public int StoppedTakeReadyControllerE() {
            int res = RiJStateReactive.TAKE_EVENT_NOT_CONSUMED;
            //## transition 4 
            if(!(lc.isOverloaded || fl.get(0).areDoorsOpened || fl.get(1).areDoorsOpened || fl.get(2).areDoorsOpened || fl.get(3).areDoorsOpened ))
                {
                    Stopped_exit();
                    Finished_entDef();
                    res = RiJStateReactive.TAKE_EVENT_COMPLETE;
                }
            return res;
        }
        
        //## statechart_method 
        public void EmergencyBaseLevelExit() {
        }
        
        //## statechart_method 
        public void EmergencyStoppedEnter() {
            //#[ state ROOT.WorkingElevator.EmergencyStopped.(Entry) 
            requests = new java.util.Vector();                
            moving = false;    
            if(effectors != null) {
            	effectors.debugMessage("EmergencyStopped entered");
            }                      
            
            
            //#]
        }
        
        //## statechart_method 
        public void rootStateEntDef() {
            WorkingElevator_entDef();
        }
        
        //## statechart_method 
        public int EmergencyMoving_takeEvent(short id) {
            int res = RiJStateReactive.TAKE_EVENT_NOT_CONSUMED;
            if(event.isTypeOf(LevelController.LevelController_Default_id))
                {
                    res = EmergencyMovingTakeLevelController();
                }
            
            if(res == RiJStateReactive.TAKE_EVENT_NOT_CONSUMED)
                {
                    res = WorkingElevator_takeEvent(id);
                }
            return res;
        }
        
        //## statechart_method 
        public void Finished_entDef() {
            Finished_enter();
        }
        
        //## statechart_method 
        public void MovingExit() {
        }
        
        //## statechart_method 
        public void MovingEnter() {
            //#[ state ROOT.WorkingElevator.Moving.(Entry) 
            moving = true;
            java.lang.Integer l = (java.lang.Integer) requests.get(0);
            requests.remove(0);
            hc.gen(new MoveControllerE(l.intValue()));         
            if(effectors != null) {
            	effectors.debugMessage("Moving entered");
            }
            //#]
        }
        
        //## statechart_method 
        public int StoppedTakeOverLoadedController() {
            OverLoadedController params = (OverLoadedController) event;
            int res = RiJStateReactive.TAKE_EVENT_NOT_CONSUMED;
            //#[ transition 8 
            for(int i = 0; i < fl.size(); i++) {
                fl.get(i).isOverloaded = false;
            }
            fl.get(params.level).isOverloaded = params.isOverloaded;
            //#]
            res = RiJStateReactive.TAKE_EVENT_COMPLETE;
            return res;
        }
        
        //## statechart_method 
        public void StoppedExit() {
        }
        
        //## statechart_method 
        public int WorkingElevatorTakeBringHere() {
            BringHere params = (BringHere) event;
            int res = RiJStateReactive.TAKE_EVENT_NOT_CONSUMED;
            WorkingElevator_exit();
            //#[ transition 16 
            requests.add(params.level);
            //#]
            WorkingElevator_enter();
            WorkingElevator_entHist();
            res = RiJStateReactive.TAKE_EVENT_COMPLETE;
            return res;
        }
        
        //## statechart_method 
        public void WorkingElevatorEnter() {
        }
        
        //## statechart_method 
        public int EmergencyBaseLevel_takeEvent(short id) {
            int res = RiJStateReactive.TAKE_EVENT_NOT_CONSUMED;
            if(event.isTypeOf(EmergencyReady.EmergencyReady_Default_id))
                {
                    res = EmergencyBaseLevelTakeEmergencyReady();
                }
            
            if(res == RiJStateReactive.TAKE_EVENT_NOT_CONSUMED)
                {
                    res = WorkingElevator_takeEvent(id);
                }
            return res;
        }
        
        //## statechart_method 
        public void EmergencyMoving_exit() {
            EmergencyMovingExit();
        }
        
        //## statechart_method 
        public void EmergencyMovingExit() {
        }
        
        //## statechart_method 
        public void Moving_entDef() {
            Moving_enter();
        }
        
        //## statechart_method 
        public void waitingForRequest_enter() {
            WorkingElevator_subState = waitingForRequest;
            rootState_active = waitingForRequest;
            waitingForRequestEnter();
        }
        
        //## statechart_method 
        public int WorkingElevatorTakeDoorsOpened() {
            DoorsOpened params = (DoorsOpened) event;
            int res = RiJStateReactive.TAKE_EVENT_NOT_CONSUMED;
            WorkingElevator_exit();
            //#[ transition 12 
            fl.get(params.level).areDoorsOpened = params.areOpened;
            //#]
            WorkingElevator_enter();
            EmergencyStopped_entDef();
            res = RiJStateReactive.TAKE_EVENT_COMPLETE;
            return res;
        }
        
        //## statechart_method 
        public void WorkingElevator_enter() {
            rootState_subState = WorkingElevator;
            WorkingElevatorEnter();
        }
        
        //## statechart_method 
        public void WorkingElevator_entDef() {
            WorkingElevator_enter();
            WorkingElevatorEntDef();
        }
        
        //## statechart_method 
        public void EmergencyStopped_exit() {
            EmergencyStoppedExit();
        }
        
        //## statechart_method 
        public int Stopped_takeEvent(short id) {
            int res = RiJStateReactive.TAKE_EVENT_NOT_CONSUMED;
            if(event.isTypeOf(OverLoadedController.OverLoadedController_Default_id))
                {
                    res = StoppedTakeOverLoadedController();
                }
            else if(event.isTypeOf(ReadyControllerE.ReadyControllerE_Default_id))
                {
                    res = StoppedTakeReadyControllerE();
                }
            else if(event.isTypeOf(MoveControllerE.MoveControllerE_Default_id))
                {
                    res = StoppedTakeMoveControllerE();
                }
            else if(event.isTypeOf(DoorsOpenedController.DoorsOpenedController_Default_id))
                {
                    res = StoppedTakeDoorsOpenedController();
                }
            
            if(res == RiJStateReactive.TAKE_EVENT_NOT_CONSUMED)
                {
                    res = WorkingElevator_takeEvent(id);
                }
            return res;
        }
        
        //## statechart_method 
        public void rootStateExit() {
        }
        
        //## statechart_method 
        public int EmergencyMovingTakeLevelController() {
            int res = RiJStateReactive.TAKE_EVENT_NOT_CONSUMED;
            EmergencyMoving_exit();
            EmergencyBaseLevel_entDef();
            res = RiJStateReactive.TAKE_EVENT_COMPLETE;
            return res;
        }
        
        //## statechart_method 
        public void Moving_exit() {
            MovingExit();
        }
        
        //## statechart_method 
        public void WorkingElevator_exit() {
            WorkingElevator_lastState = WorkingElevator_subState;
            switch (WorkingElevator_subState) {
                case EmergencyStopped:
                {
                    EmergencyStopped_exit();
                    WorkingElevator_lastState = EmergencyStopped;
                }
                break;
                case EmergencyMoving:
                {
                    EmergencyMoving_exit();
                    WorkingElevator_lastState = EmergencyMoving;
                }
                break;
                case EmergencyBaseLevel:
                {
                    EmergencyBaseLevel_exit();
                    WorkingElevator_lastState = EmergencyBaseLevel;
                }
                break;
                case Stopped:
                {
                    Stopped_exit();
                    WorkingElevator_lastState = Stopped;
                }
                break;
                case waitingForRequest:
                {
                    waitingForRequest_exit();
                    WorkingElevator_lastState = waitingForRequest;
                }
                break;
                case Finished:
                {
                    Finished_exit();
                    WorkingElevator_lastState = Finished;
                }
                break;
                case Moving:
                {
                    Moving_exit();
                    WorkingElevator_lastState = Moving;
                }
                break;
                default:
                    break;
            }
            WorkingElevator_subState = RiJNonState;
            WorkingElevatorExit();
        }
        
        //## statechart_method 
        public int EmergencyStoppedTakeEmergencyReady() {
            int res = RiJStateReactive.TAKE_EVENT_NOT_CONSUMED;
            EmergencyStopped_exit();
            waitingForRequest_entDef();
            res = RiJStateReactive.TAKE_EVENT_COMPLETE;
            return res;
        }
        
        //## statechart_method 
        public void WorkingElevatorEntDef() {
            WorkingElevator_entHist();
        }
        
    }
    //## class Elevator::ElevatorsEffectors 
    public interface ElevatorsEffectors {
        
        
        /**
         * @param message
        */
        //## operation debugMessage(String) 
        void debugMessage(final String message);
        
        /**
         * @param level
         * @param isRaised
        */
        //## operation openDoorsAlert(int,boolean) 
        void openDoorsAlert(int level, boolean isRaised);
        
        /**
         * @param level
         * @param isRaised
        */
        //## operation overloadAlert(int,boolean) 
        void overloadAlert(int level, boolean isRaised);
        
        /**
         * @param position
        */
        //## operation setPosition(double) 
        void setPosition(double position);
        
    }
}
/*********************************************************************
	File Path	: exe/DefaultConfig/Default/Elevator.java
*********************************************************************/

