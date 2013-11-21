/*********************************************************************
	Rhapsody	: 8.0.3
	Login		: janiec
	Component	: exe
	Configuration 	: DefaultConfig
	Model Element	: BringHereHandler
//!	Generated Date	: Thu, 21, Nov 2013 
	File Path	: exe/DefaultConfig/Default/BringHereHandler.java
*********************************************************************/

package Default;

//## auto_generated
import com.ibm.rational.rhapsody.oxf.*;
//## auto_generated
import com.ibm.rational.rhapsody.oxf.states.*;

//----------------------------------------------------------------------------
// Default/BringHereHandler.java                                                                  
//----------------------------------------------------------------------------

//## package Default 


//## class BringHereHandler 
public class BringHereHandler implements RiJStateConcept {
    
    public Reactive reactive;		//## ignore 
    
    protected Elevator el;		//## link el 
    
    //#[ ignore 
    public static final int RiJNonState=0;
    public static final int handle=1;
    //#]
    protected int rootState_subState;		//## ignore 
    
    protected int rootState_active;		//## ignore 
    
    
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
    public  BringHereHandler(RiJThread p_thread) {
        reactive = new Reactive(p_thread);
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
                el.__setBh(null);
            }
        __setEl(p_Elevator);
    }
    
    //## auto_generated 
    public void setEl(Elevator p_Elevator) {
        if(p_Elevator != null)
            {
                p_Elevator._setBh(this);
            }
        _setEl(p_Elevator);
    }
    
    //## auto_generated 
    public void _clearEl() {
        el = null;
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
            if(rootState_active == handle)
                {
                    res = handle_takeEvent(id);
                }
            return res;
        }
        
        //## auto_generated 
        protected void initStatechart() {
            rootState_subState = RiJNonState;
            rootState_active = RiJNonState;
        }
        
        //## statechart_method 
        public void handle_enter() {
            rootState_subState = handle;
            rootState_active = handle;
            handleEnter();
        }
        
        //## statechart_method 
        public int handleTakeBringHere0() {
            int res = RiJStateReactive.TAKE_EVENT_NOT_CONSUMED;
            //#[ transition 1 
            el.gen(new BringHere(0));
            //#]
            res = RiJStateReactive.TAKE_EVENT_COMPLETE;
            return res;
        }
        
        //## statechart_method 
        public int handleTakeBringHere1() {
            int res = RiJStateReactive.TAKE_EVENT_NOT_CONSUMED;
            //#[ transition 2 
            el.gen(new BringHere(1));
            //#]
            res = RiJStateReactive.TAKE_EVENT_COMPLETE;
            return res;
        }
        
        //## statechart_method 
        public int handleTakeBringHere2() {
            int res = RiJStateReactive.TAKE_EVENT_NOT_CONSUMED;
            //#[ transition 3 
            el.gen(new BringHere(2));
            //#]
            res = RiJStateReactive.TAKE_EVENT_COMPLETE;
            return res;
        }
        
        //## statechart_method 
        public int rootState_takeEvent(short id) {
            int res = RiJStateReactive.TAKE_EVENT_NOT_CONSUMED;
            return res;
        }
        
        //## statechart_method 
        public int handleTakeBringHere3() {
            int res = RiJStateReactive.TAKE_EVENT_NOT_CONSUMED;
            //#[ transition 4 
            el.gen(new BringHere(3));
            //#]
            res = RiJStateReactive.TAKE_EVENT_COMPLETE;
            return res;
        }
        
        //## statechart_method 
        public void handleExit() {
        }
        
        //## statechart_method 
        public void rootState_enter() {
            rootStateEnter();
        }
        
        //## statechart_method 
        public void rootStateEnter() {
        }
        
        //## statechart_method 
        public void handle_entDef() {
            handle_enter();
        }
        
        //## statechart_method 
        public void rootStateEntDef() {
            handle_entDef();
        }
        
        //## statechart_method 
        public void handleEnter() {
        }
        
        //## statechart_method 
        public void rootStateExit() {
        }
        
        //## statechart_method 
        public int handle_takeEvent(short id) {
            int res = RiJStateReactive.TAKE_EVENT_NOT_CONSUMED;
            if(event.isTypeOf(BringHere0.BringHere0_Default_id))
                {
                    res = handleTakeBringHere0();
                }
            else if(event.isTypeOf(BringHere1.BringHere1_Default_id))
                {
                    res = handleTakeBringHere1();
                }
            else if(event.isTypeOf(BringHere2.BringHere2_Default_id))
                {
                    res = handleTakeBringHere2();
                }
            else if(event.isTypeOf(BringHere3.BringHere3_Default_id))
                {
                    res = handleTakeBringHere3();
                }
            
            return res;
        }
        
        //## statechart_method 
        public void handle_exit() {
            handleExit();
        }
        
    }
}
/*********************************************************************
	File Path	: exe/DefaultConfig/Default/BringHereHandler.java
*********************************************************************/

