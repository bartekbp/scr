/*********************************************************************
	Rhapsody	: 8.0.3
	Login		: janiec
	Component	: exe
	Configuration 	: DefaultConfig
	Model Element	: Engine
//!	Generated Date	: Thu, 21, Nov 2013 
	File Path	: exe/DefaultConfig/Default/Engine.java
*********************************************************************/

package Default;

//## auto_generated
import com.ibm.rational.rhapsody.oxf.*;
//## auto_generated
import com.ibm.rational.rhapsody.oxf.states.*;

//----------------------------------------------------------------------------
// Default/Engine.java                                                                  
//----------------------------------------------------------------------------

//## package Default 


//## class Engine 
public class Engine implements RiJStateConcept {
    
    public Reactive reactive;		//## ignore 
    
    protected HeightController hc;		//## link hc 
    
    //#[ ignore 
    public static final int RiJNonState=0;
    public static final int sendaction_4=1;
    public static final int sendaction_3=2;
    public static final int NotWorking=3;
    public static final int accepteventaction_2=4;
    public static final int accepteventaction_1=5;
    //#]
    protected int rootState_subState;		//## ignore 
    
    protected int rootState_active;		//## ignore 
    
    public static final int Engine_Timeout_accepteventaction_2_id = 1;		//## ignore 
    
    public static final int Engine_Timeout_accepteventaction_1_id = 2;		//## ignore 
    
    
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
    public  Engine(RiJThread p_thread) {
        reactive = new Reactive(p_thread);
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
                hc.__setEn(null);
            }
        __setHc(p_HeightController);
    }
    
    //## auto_generated 
    public void setHc(HeightController p_HeightController) {
        if(p_HeightController != null)
            {
                p_HeightController._setEn(this);
            }
        _setHc(p_HeightController);
    }
    
    //## auto_generated 
    public void _clearHc() {
        hc = null;
    }
    
    //## auto_generated 
    public boolean startBehavior() {
        boolean done = false;
        done = reactive.startBehavior();
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
                case NotWorking:
                {
                    res = NotWorking_takeEvent(id);
                }
                break;
                case accepteventaction_1:
                {
                    res = accepteventaction_1_takeEvent(id);
                }
                break;
                case accepteventaction_2:
                {
                    res = accepteventaction_2_takeEvent(id);
                }
                break;
                case sendaction_3:
                {
                    res = sendaction_3_takeEvent(id);
                }
                break;
                case sendaction_4:
                {
                    res = sendaction_4_takeEvent(id);
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
        }
        
        //## statechart_method 
        public void accepteventaction_2Enter() {
            itsRiJThread.schedTimeout(3000, Engine_Timeout_accepteventaction_2_id, this, null);
        }
        
        //## statechart_method 
        public void sendaction_3_exit() {
            popNullConfig();
            sendaction_3Exit();
        }
        
        //## statechart_method 
        public void accepteventaction_1Exit() {
            itsRiJThread.unschedTimeout(Engine_Timeout_accepteventaction_1_id, this);
        }
        
        //## statechart_method 
        public void accepteventaction_1Enter() {
            itsRiJThread.schedTimeout(3000, Engine_Timeout_accepteventaction_1_id, this, null);
        }
        
        //## statechart_method 
        public int NotWorkingTakeUp() {
            int res = RiJStateReactive.TAKE_EVENT_NOT_CONSUMED;
            NotWorking_exit();
            accepteventaction_2_entDef();
            res = RiJStateReactive.TAKE_EVENT_COMPLETE;
            return res;
        }
        
        //## statechart_method 
        public void sendaction_3Exit() {
        }
        
        //## statechart_method 
        public int accepteventaction_1_takeEvent(short id) {
            int res = RiJStateReactive.TAKE_EVENT_NOT_CONSUMED;
            if(event.isTypeOf(RiJEvent.TIMEOUT_EVENT_ID))
                {
                    res = accepteventaction_1TakeRiJTimeout();
                }
            
            return res;
        }
        
        //## statechart_method 
        public void accepteventaction_2Exit() {
            itsRiJThread.unschedTimeout(Engine_Timeout_accepteventaction_2_id, this);
        }
        
        //## statechart_method 
        public void sendaction_4Exit() {
        }
        
        //## statechart_method 
        public int accepteventaction_2TakeRiJTimeout() {
            int res = RiJStateReactive.TAKE_EVENT_NOT_CONSUMED;
            if(event.getTimeoutId() == Engine_Timeout_accepteventaction_2_id)
                {
                    accepteventaction_2_exit();
                    sendaction_3_entDef();
                    res = RiJStateReactive.TAKE_EVENT_COMPLETE;
                }
            return res;
        }
        
        //## statechart_method 
        public void accepteventaction_2_exit() {
            accepteventaction_2Exit();
        }
        
        //## statechart_method 
        public void accepteventaction_1_exit() {
            accepteventaction_1Exit();
        }
        
        //## statechart_method 
        public void accepteventaction_1_enter() {
            rootState_subState = accepteventaction_1;
            rootState_active = accepteventaction_1;
            accepteventaction_1Enter();
        }
        
        //## statechart_method 
        public void sendaction_3_entDef() {
            sendaction_3_enter();
        }
        
        //## statechart_method 
        public void accepteventaction_1_entDef() {
            accepteventaction_1_enter();
        }
        
        //## statechart_method 
        public void accepteventaction_2_enter() {
            rootState_subState = accepteventaction_2;
            rootState_active = accepteventaction_2;
            accepteventaction_2Enter();
        }
        
        //## statechart_method 
        public int sendaction_4TakeNull() {
            int res = RiJStateReactive.TAKE_EVENT_NOT_CONSUMED;
            sendaction_4_exit();
            NotWorking_entDef();
            res = RiJStateReactive.TAKE_EVENT_COMPLETE;
            return res;
        }
        
        //## statechart_method 
        public void sendaction_3_enter() {
            pushNullConfig();
            rootState_subState = sendaction_3;
            rootState_active = sendaction_3;
            sendaction_3Enter();
        }
        
        //## statechart_method 
        public int rootState_takeEvent(short id) {
            int res = RiJStateReactive.TAKE_EVENT_NOT_CONSUMED;
            return res;
        }
        
        //## statechart_method 
        public void NotWorkingExit() {
        }
        
        //## statechart_method 
        public void sendaction_4_enter() {
            pushNullConfig();
            rootState_subState = sendaction_4;
            rootState_active = sendaction_4;
            sendaction_4Enter();
        }
        
        //## statechart_method 
        public int sendaction_3TakeNull() {
            int res = RiJStateReactive.TAKE_EVENT_NOT_CONSUMED;
            sendaction_3_exit();
            NotWorking_entDef();
            res = RiJStateReactive.TAKE_EVENT_COMPLETE;
            return res;
        }
        
        //## statechart_method 
        public int sendaction_4_takeEvent(short id) {
            int res = RiJStateReactive.TAKE_EVENT_NOT_CONSUMED;
            if(event.isTypeOf(RiJEvent.NULL_EVENT_ID))
                {
                    res = sendaction_4TakeNull();
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
        public void NotWorking_enter() {
            rootState_subState = NotWorking;
            rootState_active = NotWorking;
            NotWorkingEnter();
        }
        
        //## statechart_method 
        public void NotWorkingEnter() {
        }
        
        //## statechart_method 
        public void sendaction_4_entDef() {
            sendaction_4_enter();
        }
        
        //## statechart_method 
        public void accepteventaction_2_entDef() {
            accepteventaction_2_enter();
        }
        
        //## statechart_method 
        public int NotWorking_takeEvent(short id) {
            int res = RiJStateReactive.TAKE_EVENT_NOT_CONSUMED;
            if(event.isTypeOf(Down.Down_Default_id))
                {
                    res = NotWorkingTakeDown();
                }
            else if(event.isTypeOf(Up.Up_Default_id))
                {
                    res = NotWorkingTakeUp();
                }
            
            return res;
        }
        
        //## statechart_method 
        public void rootStateEntDef() {
            NotWorking_entDef();
        }
        
        //## statechart_method 
        public int accepteventaction_1TakeRiJTimeout() {
            int res = RiJStateReactive.TAKE_EVENT_NOT_CONSUMED;
            if(event.getTimeoutId() == Engine_Timeout_accepteventaction_1_id)
                {
                    accepteventaction_1_exit();
                    sendaction_4_entDef();
                    res = RiJStateReactive.TAKE_EVENT_COMPLETE;
                }
            return res;
        }
        
        //## statechart_method 
        public int NotWorkingTakeDown() {
            int res = RiJStateReactive.TAKE_EVENT_NOT_CONSUMED;
            NotWorking_exit();
            accepteventaction_1_entDef();
            res = RiJStateReactive.TAKE_EVENT_COMPLETE;
            return res;
        }
        
        //## statechart_method 
        public void NotWorking_exit() {
            NotWorkingExit();
        }
        
        //## statechart_method 
        public void NotWorking_entDef() {
            NotWorking_enter();
        }
        
        //## statechart_method 
        public int sendaction_3_takeEvent(short id) {
            int res = RiJStateReactive.TAKE_EVENT_NOT_CONSUMED;
            if(event.isTypeOf(RiJEvent.NULL_EVENT_ID))
                {
                    res = sendaction_3TakeNull();
                }
            
            return res;
        }
        
        //## statechart_method 
        public void sendaction_4Enter() {
            //#[ state ROOT.sendaction_4.(Entry) 
            hc.gen(new Default.Down());
            //#]
        }
        
        //## statechart_method 
        public int accepteventaction_2_takeEvent(short id) {
            int res = RiJStateReactive.TAKE_EVENT_NOT_CONSUMED;
            if(event.isTypeOf(RiJEvent.TIMEOUT_EVENT_ID))
                {
                    res = accepteventaction_2TakeRiJTimeout();
                }
            
            return res;
        }
        
        //## statechart_method 
        public void sendaction_3Enter() {
            //#[ state ROOT.sendaction_3.(Entry) 
            hc.gen(new Default.Up());
            //#]
        }
        
        //## statechart_method 
        public void rootStateExit() {
        }
        
        //## statechart_method 
        public void sendaction_4_exit() {
            popNullConfig();
            sendaction_4Exit();
        }
        
    }
}
/*********************************************************************
	File Path	: exe/DefaultConfig/Default/Engine.java
*********************************************************************/

