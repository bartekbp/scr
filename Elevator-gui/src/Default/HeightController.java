/*********************************************************************
	Rhapsody	: 8.0.3
	Login		: janiec
	Component	: exe
	Configuration 	: DefaultConfig
	Model Element	: HeightController
//!	Generated Date	: Fri, 22, Nov 2013 
	File Path	: exe/DefaultConfig/Default/HeightController.java
*********************************************************************/

package Default;

//## auto_generated
import com.ibm.rational.rhapsody.oxf.*;
//## auto_generated
import com.ibm.rational.rhapsody.oxf.states.*;

//----------------------------------------------------------------------------
// Default/HeightController.java                                                                  
//----------------------------------------------------------------------------

//## package Default 


//## class HeightController 
public class HeightController implements RiJStateConcept {
    
    public Reactive reactive;		//## ignore 
    
    protected int desiredLevel;		//## attribute desiredLevel 
    
    protected final double epsilion = 0.0001;		//## attribute epsilion 
    
    protected double level;		//## attribute level 
    
    protected final double step = 1.0/16.0;		//## attribute step 
    
    protected Elevator el;		//## link el 
    
    protected Engine en;		//## classInstance en 
    
    //#[ ignore 
    public static final int RiJNonState=0;
    public static final int state_14=1;
    public static final int SendEvent=2;
    public static final int sendaction_6=3;
    public static final int sendaction_5=4;
    public static final int MovingDecision=5;
    public static final int Init=6;
    public static final int BeforeWaitingForEvent=7;
    //#]
    protected int rootState_subState;		//## ignore 
    
    protected int rootState_active;		//## ignore 
    
    protected int state_14_subState;		//## ignore 
    
    
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
    public  HeightController(RiJThread p_thread) {
        reactive = new Reactive(p_thread);
        initRelations(p_thread);
    }
    
    //## TriggeredOperation Stop() 
    public void Stop() {
        Stop_HeightController_Event triggerEvent = new Stop_HeightController_Event();
        reactive.takeTrigger(triggerEvent);
    }
    
    //## operation getLevel() 
    public int getLevel() {
        //#[ operation getLevel() 
        return (int)(level + epsilion);
        //#]
    }
    
    //## auto_generated 
    public int getDesiredLevel() {
        return desiredLevel;
    }
    
    //## auto_generated 
    public void setDesiredLevel(int p_desiredLevel) {
        desiredLevel = p_desiredLevel;
    }
    
    //## auto_generated 
    public final double getEpsilion() {
        return epsilion;
    }
    
    //## auto_generated 
    public void setLevel(double p_level) {
        level = p_level;
    }
    
    //## auto_generated 
    public final double getStep() {
        return step;
    }
    
    //## auto_generated 
    public Elevator getEl() {
        return el;
    }
    
    //## auto_generated 
    public void __setEl(Elevator p_Elevator) {
        el = p_Elevator;
    }
    
    //## auto_generated 
    public void _setEl(Elevator p_Elevator) {
        if(el != null)
            {
                el.__setHc(null);
            }
        __setEl(p_Elevator);
    }
    
    //## auto_generated 
    public void setEl(Elevator p_Elevator) {
        if(p_Elevator != null)
            {
                p_Elevator._setHc(this);
            }
        _setEl(p_Elevator);
    }
    
    //## auto_generated 
    public void _clearEl() {
        el = null;
    }
    
    //## auto_generated 
    public Engine getEn() {
        return en;
    }
    
    //## auto_generated 
    public void __setEn(Engine p_Engine) {
        en = p_Engine;
    }
    
    //## auto_generated 
    public void _setEn(Engine p_Engine) {
        if(en != null)
            {
                en.__setHc(null);
            }
        __setEn(p_Engine);
    }
    
    //## auto_generated 
    public Engine newEn(RiJThread p_thread) {
        en = new Engine(p_thread);
        en._setHc(this);
        return en;
    }
    
    //## auto_generated 
    public void deleteEn() {
        en.__setHc(null);
        en=null;
    }
    
    //## auto_generated 
    protected void initRelations(RiJThread p_thread) {
        en = newEn(p_thread);
    }
    
    //## auto_generated 
    public boolean startBehavior() {
        boolean done = true;
        done &= en.startBehavior();
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
            if(state_14_subState == state)
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
                case MovingDecision:
                {
                    res = MovingDecision_takeEvent(id);
                }
                break;
                case BeforeWaitingForEvent:
                {
                    res = BeforeWaitingForEvent_takeEvent(id);
                }
                break;
                case sendaction_6:
                {
                    res = sendaction_6_takeEvent(id);
                }
                break;
                case Init:
                {
                    res = Init_takeEvent(id);
                }
                break;
                case sendaction_5:
                {
                    res = sendaction_5_takeEvent(id);
                }
                break;
                case SendEvent:
                {
                    res = SendEvent_takeEvent(id);
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
            state_14_subState = RiJNonState;
        }
        
        //## statechart_method 
        public void SendEvent_entDef() {
            SendEvent_enter();
        }
        
        //## statechart_method 
        public int sendaction_5TakeNull() {
            int res = RiJStateReactive.TAKE_EVENT_NOT_CONSUMED;
            sendaction_5_exit();
            BeforeWaitingForEvent_entDef();
            res = RiJStateReactive.TAKE_EVENT_COMPLETE;
            return res;
        }
        
        //## statechart_method 
        public void BeforeWaitingForEvent_enter() {
            state_14_subState = BeforeWaitingForEvent;
            rootState_active = BeforeWaitingForEvent;
            BeforeWaitingForEventEnter();
        }
        
        //## statechart_method 
        public int InitTakeMoveControllerE() {
            MoveControllerE params = (MoveControllerE) event;
            int res = RiJStateReactive.TAKE_EVENT_NOT_CONSUMED;
            Init_exit();
            //#[ transition 1 
            desiredLevel = params.level;
            //#]
            MovingDecision_entDef();
            res = RiJStateReactive.TAKE_EVENT_COMPLETE;
            return res;
        }
        
        //## statechart_method 
        public void InitEnter() {
        }
        
        //## statechart_method 
        public int sendaction_5_takeEvent(short id) {
            int res = RiJStateReactive.TAKE_EVENT_NOT_CONSUMED;
            if(event.isTypeOf(RiJEvent.NULL_EVENT_ID))
                {
                    res = sendaction_5TakeNull();
                }
            
            if(res == RiJStateReactive.TAKE_EVENT_NOT_CONSUMED)
                {
                    res = state_14_takeEvent(id);
                }
            return res;
        }
        
        //## statechart_method 
        public void MovingDecisionExit() {
        }
        
        //## statechart_method 
        public void MovingDecision_enter() {
            pushNullConfig();
            state_14_subState = MovingDecision;
            rootState_active = MovingDecision;
            MovingDecisionEnter();
        }
        
        //## statechart_method 
        public void sendaction_5Exit() {
        }
        
        //## statechart_method 
        public int state_14TakeStop() {
            int res = RiJStateReactive.TAKE_EVENT_NOT_CONSUMED;
            state_14_exit();
            state_14_enter();
            Init_entDef();
            res = RiJStateReactive.TAKE_EVENT_COMPLETE;
            return res;
        }
        
        //## statechart_method 
        public void state_14_enter() {
            rootState_subState = state_14;
            state_14Enter();
        }
        
        //## statechart_method 
        public void BeforeWaitingForEvent_entDef() {
            BeforeWaitingForEvent_enter();
        }
        
        //## statechart_method 
        public void sendaction_6Exit() {
        }
        
        //## statechart_method 
        public int SendEventTakeMoveControllerE() {
            MoveControllerE params = (MoveControllerE) event;
            int res = RiJStateReactive.TAKE_EVENT_NOT_CONSUMED;
            SendEvent_exit();
            //#[ transition 9 
            desiredLevel = params.level;
            //#]
            MovingDecision_entDef();
            res = RiJStateReactive.TAKE_EVENT_COMPLETE;
            return res;
        }
        
        //## statechart_method 
        public void SendEventExit() {
        }
        
        //## statechart_method 
        public void Init_exit() {
            InitExit();
        }
        
        //## statechart_method 
        public void Init_entDef() {
            Init_enter();
        }
        
        //## statechart_method 
        public void sendaction_6_entDef() {
            sendaction_6_enter();
        }
        
        //## statechart_method 
        public void MovingDecision_entDef() {
            MovingDecision_enter();
        }
        
        //## statechart_method 
        public int SendEvent_takeEvent(short id) {
            int res = RiJStateReactive.TAKE_EVENT_NOT_CONSUMED;
            if(event.isTypeOf(MoveControllerE.MoveControllerE_Default_id))
                {
                    res = SendEventTakeMoveControllerE();
                }
            
            if(res == RiJStateReactive.TAKE_EVENT_NOT_CONSUMED)
                {
                    res = state_14_takeEvent(id);
                }
            return res;
        }
        
        //## statechart_method 
        public void state_14Enter() {
        }
        
        //## statechart_method 
        public int rootState_takeEvent(short id) {
            int res = RiJStateReactive.TAKE_EVENT_NOT_CONSUMED;
            return res;
        }
        
        //## statechart_method 
        public void sendaction_5_enter() {
            pushNullConfig();
            state_14_subState = sendaction_5;
            rootState_active = sendaction_5;
            sendaction_5Enter();
        }
        
        //## statechart_method 
        public void SendEventEnter() {
            //#[ state ROOT.state_14.SendEvent.(Entry) 
            el.gen(new LevelController());
            //#]
        }
        
        //## statechart_method 
        public void state_14_entDef() {
            state_14_enter();
            
            Init_entDef();
        }
        
        //## statechart_method 
        public void sendaction_6_enter() {
            pushNullConfig();
            state_14_subState = sendaction_6;
            rootState_active = sendaction_6;
            sendaction_6Enter();
        }
        
        //## statechart_method 
        public int state_14_takeEvent(short id) {
            int res = RiJStateReactive.TAKE_EVENT_NOT_CONSUMED;
            if(event.isTypeOf(Stop.Stop_Default_id))
                {
                    res = state_14TakeStop();
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
        public void BeforeWaitingForEventExit() {
        }
        
        //## statechart_method 
        public int MovingDecision_takeEvent(short id) {
            int res = RiJStateReactive.TAKE_EVENT_NOT_CONSUMED;
            if(event.isTypeOf(RiJEvent.NULL_EVENT_ID))
                {
                    res = MovingDecisionTakeNull();
                }
            
            if(res == RiJStateReactive.TAKE_EVENT_NOT_CONSUMED)
                {
                    res = state_14_takeEvent(id);
                }
            return res;
        }
        
        //## statechart_method 
        public void state_14_exit() {
            switch (state_14_subState) {
                case MovingDecision:
                {
                    MovingDecision_exit();
                }
                break;
                case BeforeWaitingForEvent:
                {
                    BeforeWaitingForEvent_exit();
                }
                break;
                case sendaction_6:
                {
                    sendaction_6_exit();
                }
                break;
                case Init:
                {
                    Init_exit();
                }
                break;
                case sendaction_5:
                {
                    sendaction_5_exit();
                }
                break;
                case SendEvent:
                {
                    SendEvent_exit();
                }
                break;
                default:
                    break;
            }
            state_14_subState = RiJNonState;
            state_14Exit();
        }
        
        //## statechart_method 
        public void SendEvent_exit() {
            SendEventExit();
        }
        
        //## statechart_method 
        public void state_14Exit() {
        }
        
        //## statechart_method 
        public int BeforeWaitingForEventTakeUp() {
            int res = RiJStateReactive.TAKE_EVENT_NOT_CONSUMED;
            BeforeWaitingForEvent_exit();
            //#[ transition 8 
            level = level + step;
            //#]
            MovingDecision_entDef();
            res = RiJStateReactive.TAKE_EVENT_COMPLETE;
            return res;
        }
        
        //## statechart_method 
        public void sendaction_6Enter() {
            //#[ state ROOT.state_14.sendaction_6.(Entry) 
            en.gen(new Default.Up());
            //#]
        }
        
        //## statechart_method 
        public void rootStateEntDef() {
            state_14_entDef();
        }
        
        //## statechart_method 
        public void sendaction_5Enter() {
            //#[ state ROOT.state_14.sendaction_5.(Entry) 
            en.gen(new Default.Down());
            //#]
        }
        
        //## statechart_method 
        public void SendEvent_enter() {
            state_14_subState = SendEvent;
            rootState_active = SendEvent;
            SendEventEnter();
        }
        
        //## statechart_method 
        public int BeforeWaitingForEvent_takeEvent(short id) {
            int res = RiJStateReactive.TAKE_EVENT_NOT_CONSUMED;
            if(event.isTypeOf(Down.Down_Default_id))
                {
                    res = BeforeWaitingForEventTakeDown();
                }
            else if(event.isTypeOf(Up.Up_Default_id))
                {
                    res = BeforeWaitingForEventTakeUp();
                }
            
            if(res == RiJStateReactive.TAKE_EVENT_NOT_CONSUMED)
                {
                    res = state_14_takeEvent(id);
                }
            return res;
        }
        
        //## statechart_method 
        public int BeforeWaitingForEventTakeDown() {
            int res = RiJStateReactive.TAKE_EVENT_NOT_CONSUMED;
            BeforeWaitingForEvent_exit();
            //#[ transition 7 
            level = level - step;
            //#]
            MovingDecision_entDef();
            res = RiJStateReactive.TAKE_EVENT_COMPLETE;
            return res;
        }
        
        //## statechart_method 
        public void BeforeWaitingForEventEnter() {
        }
        
        //## statechart_method 
        public void MovingDecisionEnter() {
            //#[ state ROOT.state_14.MovingDecision.(Entry) 
            if(el.effectors != null) {
            	el.effectors.setPosition(level);
            }
            //#]
        }
        
        //## statechart_method 
        public void Init_enter() {
            state_14_subState = Init;
            rootState_active = Init;
            InitEnter();
        }
        
        //## statechart_method 
        public int sendaction_6_takeEvent(short id) {
            int res = RiJStateReactive.TAKE_EVENT_NOT_CONSUMED;
            if(event.isTypeOf(RiJEvent.NULL_EVENT_ID))
                {
                    res = sendaction_6TakeNull();
                }
            
            if(res == RiJStateReactive.TAKE_EVENT_NOT_CONSUMED)
                {
                    res = state_14_takeEvent(id);
                }
            return res;
        }
        
        //## statechart_method 
        public void sendaction_6_exit() {
            popNullConfig();
            sendaction_6Exit();
        }
        
        //## statechart_method 
        public void rootStateExit() {
        }
        
        //## statechart_method 
        public void InitExit() {
        }
        
        //## statechart_method 
        public int MovingDecisionTakeNull() {
            int res = RiJStateReactive.TAKE_EVENT_NOT_CONSUMED;
            //## transition 2 
            if(Math.abs(desiredLevel - level) < epsilion)
                {
                    MovingDecision_exit();
                    //#[ transition 2 
                    level = desiredLevel;
                    //#]
                    SendEvent_entDef();
                    res = RiJStateReactive.TAKE_EVENT_COMPLETE;
                }
            else
                {
                    //## transition 3 
                    if(desiredLevel < level)
                        {
                            MovingDecision_exit();
                            sendaction_5_entDef();
                            res = RiJStateReactive.TAKE_EVENT_COMPLETE;
                        }
                    else
                        {
                            //## transition 4 
                            if(desiredLevel > level)
                                {
                                    MovingDecision_exit();
                                    sendaction_6_entDef();
                                    res = RiJStateReactive.TAKE_EVENT_COMPLETE;
                                }
                        }
                }
            return res;
        }
        
        //## statechart_method 
        public void sendaction_5_exit() {
            popNullConfig();
            sendaction_5Exit();
        }
        
        //## statechart_method 
        public int sendaction_6TakeNull() {
            int res = RiJStateReactive.TAKE_EVENT_NOT_CONSUMED;
            sendaction_6_exit();
            BeforeWaitingForEvent_entDef();
            res = RiJStateReactive.TAKE_EVENT_COMPLETE;
            return res;
        }
        
        //## statechart_method 
        public void BeforeWaitingForEvent_exit() {
            BeforeWaitingForEventExit();
        }
        
        //## statechart_method 
        public int Init_takeEvent(short id) {
            int res = RiJStateReactive.TAKE_EVENT_NOT_CONSUMED;
            if(event.isTypeOf(MoveControllerE.MoveControllerE_Default_id))
                {
                    res = InitTakeMoveControllerE();
                }
            
            if(res == RiJStateReactive.TAKE_EVENT_NOT_CONSUMED)
                {
                    res = state_14_takeEvent(id);
                }
            return res;
        }
        
        //## statechart_method 
        public void MovingDecision_exit() {
            popNullConfig();
            MovingDecisionExit();
        }
        
        //## statechart_method 
        public void sendaction_5_entDef() {
            sendaction_5_enter();
        }
        
    }
}
//## ignore 
class Stop_HeightController_Event extends RiJEvent {
    
    public static final int Stop_HeightController_Event_id = 31000;
    
    // Constructors
    
    public  Stop_HeightController_Event() {
        lId = Stop_HeightController_Event_id;
    }
    
}
/*********************************************************************
	File Path	: exe/DefaultConfig/Default/HeightController.java
*********************************************************************/

