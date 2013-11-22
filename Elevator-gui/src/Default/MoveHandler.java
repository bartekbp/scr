/*********************************************************************
	Rhapsody	: 8.0.3
	Login		: janiec
	Component	: exe
	Configuration 	: DefaultConfig
	Model Element	: MoveHandler
//!	Generated Date	: Fri, 22, Nov 2013 
	File Path	: exe/DefaultConfig/Default/MoveHandler.java
*********************************************************************/

package Default;

//## auto_generated
import com.ibm.rational.rhapsody.oxf.*;
//## auto_generated
import com.ibm.rational.rhapsody.oxf.states.*;

//----------------------------------------------------------------------------
// Default/MoveHandler.java                                                                  
//----------------------------------------------------------------------------

//## package Default 


//## class MoveHandler 
public class MoveHandler implements RiJStateConcept {
    
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
    public  MoveHandler(RiJThread p_thread) {
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
                el.__setMh(null);
            }
        __setEl(p_Elevator);
    }
    
    //## auto_generated 
    public void setEl(Elevator p_Elevator) {
        if(p_Elevator != null)
            {
                p_Elevator._setMh(this);
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
        public int handleTakeMove30() {
            int res = RiJStateReactive.TAKE_EVENT_NOT_CONSUMED;
            //#[ transition 13 
            el.mc.gen(new Move(3,0));
            //#]
            res = RiJStateReactive.TAKE_EVENT_COMPLETE;
            return res;
        }
        
        //## statechart_method 
        public int handleTakeMove31() {
            int res = RiJStateReactive.TAKE_EVENT_NOT_CONSUMED;
            //#[ transition 14 
            el.mc.gen(new Move(3,1));
            //#]
            res = RiJStateReactive.TAKE_EVENT_COMPLETE;
            return res;
        }
        
        //## statechart_method 
        public int handleTakeMove20() {
            int res = RiJStateReactive.TAKE_EVENT_NOT_CONSUMED;
            //#[ transition 9 
            el.mc.gen(new Move(2,0));
            //#]
            res = RiJStateReactive.TAKE_EVENT_COMPLETE;
            return res;
        }
        
        //## statechart_method 
        public int handleTakeMove32() {
            int res = RiJStateReactive.TAKE_EVENT_NOT_CONSUMED;
            //#[ transition 15 
            el.mc.gen(new Move(3,2));
            //#]
            res = RiJStateReactive.TAKE_EVENT_COMPLETE;
            return res;
        }
        
        //## statechart_method 
        public int handleTakeMove21() {
            int res = RiJStateReactive.TAKE_EVENT_NOT_CONSUMED;
            //#[ transition 10 
            el.mc.gen(new Move(2,1));
            //#]
            res = RiJStateReactive.TAKE_EVENT_COMPLETE;
            return res;
        }
        
        //## statechart_method 
        public int handleTakeMove10() {
            int res = RiJStateReactive.TAKE_EVENT_NOT_CONSUMED;
            //#[ transition 5 
            el.mc.gen(new Move(1,0));
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
        public int handleTakeMove33() {
            int res = RiJStateReactive.TAKE_EVENT_NOT_CONSUMED;
            //#[ transition 16 
            el.mc.gen(new Move(3,3));
            //#]
            res = RiJStateReactive.TAKE_EVENT_COMPLETE;
            return res;
        }
        
        //## statechart_method 
        public int handleTakeMove22() {
            int res = RiJStateReactive.TAKE_EVENT_NOT_CONSUMED;
            //#[ transition 11 
            el.mc.gen(new Move(2,2));
            //#]
            res = RiJStateReactive.TAKE_EVENT_COMPLETE;
            return res;
        }
        
        //## statechart_method 
        public int handleTakeMove11() {
            int res = RiJStateReactive.TAKE_EVENT_NOT_CONSUMED;
            //#[ transition 6 
            el.mc.gen(new Move(1,1));
            //#]
            res = RiJStateReactive.TAKE_EVENT_COMPLETE;
            return res;
        }
        
        //## statechart_method 
        public int handleTakeMove00() {
            int res = RiJStateReactive.TAKE_EVENT_NOT_CONSUMED;
            //#[ transition 1 
            el.mc.gen(new Move(0, 0));
            //#]
            res = RiJStateReactive.TAKE_EVENT_COMPLETE;
            return res;
        }
        
        //## statechart_method 
        public void handleExit() {
        }
        
        //## statechart_method 
        public int handleTakeMove23() {
            int res = RiJStateReactive.TAKE_EVENT_NOT_CONSUMED;
            //#[ transition 12 
            el.mc.gen(new Move(2,3));
            //#]
            res = RiJStateReactive.TAKE_EVENT_COMPLETE;
            return res;
        }
        
        //## statechart_method 
        public int handleTakeMove12() {
            int res = RiJStateReactive.TAKE_EVENT_NOT_CONSUMED;
            //#[ transition 7 
            el.mc.gen(new Move(1,2));
            //#]
            res = RiJStateReactive.TAKE_EVENT_COMPLETE;
            return res;
        }
        
        //## statechart_method 
        public int handleTakeMove01() {
            int res = RiJStateReactive.TAKE_EVENT_NOT_CONSUMED;
            //#[ transition 2 
            el.mc.gen(new Move(0,1));
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
        public int handleTakeMove13() {
            int res = RiJStateReactive.TAKE_EVENT_NOT_CONSUMED;
            //#[ transition 8 
            el.mc.gen(new Move(1,3));
            //#]
            res = RiJStateReactive.TAKE_EVENT_COMPLETE;
            return res;
        }
        
        //## statechart_method 
        public int handleTakeMove02() {
            int res = RiJStateReactive.TAKE_EVENT_NOT_CONSUMED;
            //#[ transition 3 
            el.mc.gen(new Move(0,2));
            //#]
            res = RiJStateReactive.TAKE_EVENT_COMPLETE;
            return res;
        }
        
        //## statechart_method 
        public int handleTakeMove03() {
            int res = RiJStateReactive.TAKE_EVENT_NOT_CONSUMED;
            //#[ transition 4 
            el.mc.gen(new Move(0,3));
            //#]
            res = RiJStateReactive.TAKE_EVENT_COMPLETE;
            return res;
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
            if(event.isTypeOf(Move33.Move33_Default_id))
                {
                    res = handleTakeMove33();
                }
            else if(event.isTypeOf(Move22.Move22_Default_id))
                {
                    res = handleTakeMove22();
                }
            else if(event.isTypeOf(Move11.Move11_Default_id))
                {
                    res = handleTakeMove11();
                }
            else if(event.isTypeOf(Move00.Move00_Default_id))
                {
                    res = handleTakeMove00();
                }
            else if(event.isTypeOf(Move23.Move23_Default_id))
                {
                    res = handleTakeMove23();
                }
            else if(event.isTypeOf(Move12.Move12_Default_id))
                {
                    res = handleTakeMove12();
                }
            else if(event.isTypeOf(Move01.Move01_Default_id))
                {
                    res = handleTakeMove01();
                }
            else if(event.isTypeOf(Move13.Move13_Default_id))
                {
                    res = handleTakeMove13();
                }
            else if(event.isTypeOf(Move02.Move02_Default_id))
                {
                    res = handleTakeMove02();
                }
            else if(event.isTypeOf(Move03.Move03_Default_id))
                {
                    res = handleTakeMove03();
                }
            else if(event.isTypeOf(Move30.Move30_Default_id))
                {
                    res = handleTakeMove30();
                }
            else if(event.isTypeOf(Move31.Move31_Default_id))
                {
                    res = handleTakeMove31();
                }
            else if(event.isTypeOf(Move20.Move20_Default_id))
                {
                    res = handleTakeMove20();
                }
            else if(event.isTypeOf(Move32.Move32_Default_id))
                {
                    res = handleTakeMove32();
                }
            else if(event.isTypeOf(Move21.Move21_Default_id))
                {
                    res = handleTakeMove21();
                }
            else if(event.isTypeOf(Move10.Move10_Default_id))
                {
                    res = handleTakeMove10();
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
	File Path	: exe/DefaultConfig/Default/MoveHandler.java
*********************************************************************/

