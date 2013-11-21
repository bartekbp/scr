/*********************************************************************
	Rhapsody	: 8.0.3
	Login		: janiec
	Component	: exe
	Configuration 	: DefaultConfig
	Model Element	: DoorsOpenedHandler
//!	Generated Date	: Thu, 21, Nov 2013 
	File Path	: exe/DefaultConfig/Default/DoorsOpenedHandler.java
*********************************************************************/

package Default;

//## auto_generated
import com.ibm.rational.rhapsody.oxf.*;
//## auto_generated
import com.ibm.rational.rhapsody.oxf.states.*;

//----------------------------------------------------------------------------
// Default/DoorsOpenedHandler.java                                                                  
//----------------------------------------------------------------------------

//## package Default 


//## class DoorsOpenedHandler 
public class DoorsOpenedHandler implements RiJStateConcept {
    
    public Reactive reactive;		//## ignore 
    
    protected boolean base;		//## attribute base 
    
    protected boolean first;		//## attribute first 
    
    protected boolean snd;		//## attribute snd 
    
    protected boolean thd;		//## attribute thd 
    
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
    public  DoorsOpenedHandler(RiJThread p_thread) {
        reactive = new Reactive(p_thread);
    }
    
    //## auto_generated 
    public boolean getBase() {
        return base;
    }
    
    //## auto_generated 
    public void setBase(boolean p_base) {
        base = p_base;
    }
    
    //## auto_generated 
    public boolean getFirst() {
        return first;
    }
    
    //## auto_generated 
    public void setFirst(boolean p_first) {
        first = p_first;
    }
    
    //## auto_generated 
    public boolean getSnd() {
        return snd;
    }
    
    //## auto_generated 
    public void setSnd(boolean p_snd) {
        snd = p_snd;
    }
    
    //## auto_generated 
    public boolean getThd() {
        return thd;
    }
    
    //## auto_generated 
    public void setThd(boolean p_thd) {
        thd = p_thd;
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
                el.__setDh(null);
            }
        __setEl(p_Elevator);
    }
    
    //## auto_generated 
    public void setEl(Elevator p_Elevator) {
        if(p_Elevator != null)
            {
                p_Elevator._setDh(this);
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
        public int handleTakeDoorsOpened0() {
            int res = RiJStateReactive.TAKE_EVENT_NOT_CONSUMED;
            //#[ transition 1 
            base ^= true;
            el.dc.gen(new DoorsOpened(0, base));
            //#]
            res = RiJStateReactive.TAKE_EVENT_COMPLETE;
            return res;
        }
        
        //## statechart_method 
        public int handleTakeDoorsOpened1() {
            int res = RiJStateReactive.TAKE_EVENT_NOT_CONSUMED;
            //#[ transition 2 
            first ^= true;
            el.dc.gen(new DoorsOpened(1, first));
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
        public int handleTakeDoorsOpened2() {
            int res = RiJStateReactive.TAKE_EVENT_NOT_CONSUMED;
            //#[ transition 3 
            snd ^= true;
            el.dc.gen(new DoorsOpened(2, snd));
            //#]
            res = RiJStateReactive.TAKE_EVENT_COMPLETE;
            return res;
        }
        
        //## statechart_method 
        public void handleExit() {
        }
        
        //## statechart_method 
        public int handleTakeDoorsOpened3() {
            int res = RiJStateReactive.TAKE_EVENT_NOT_CONSUMED;
            //#[ transition 4 
            thd ^= true;
            el.dc.gen(new DoorsOpened(3, thd));
            //#]
            res = RiJStateReactive.TAKE_EVENT_COMPLETE;
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
            if(event.isTypeOf(DoorsOpened0.DoorsOpened0_Default_id))
                {
                    res = handleTakeDoorsOpened0();
                }
            else if(event.isTypeOf(DoorsOpened1.DoorsOpened1_Default_id))
                {
                    res = handleTakeDoorsOpened1();
                }
            else if(event.isTypeOf(DoorsOpened2.DoorsOpened2_Default_id))
                {
                    res = handleTakeDoorsOpened2();
                }
            else if(event.isTypeOf(DoorsOpened3.DoorsOpened3_Default_id))
                {
                    res = handleTakeDoorsOpened3();
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
	File Path	: exe/DefaultConfig/Default/DoorsOpenedHandler.java
*********************************************************************/

