/*********************************************************************
	Rhapsody	: 8.0.3
	Login		: janiec
	Component	: exe
	Configuration 	: DefaultConfig
	Model Element	: ReadyController
//!	Generated Date	: Fri, 22, Nov 2013 
	File Path	: exe/DefaultConfig/Default/ReadyController.java
*********************************************************************/

package Default;

//## auto_generated
import com.ibm.rational.rhapsody.oxf.*;
//## auto_generated
import com.ibm.rational.rhapsody.oxf.states.*;

//----------------------------------------------------------------------------
// Default/ReadyController.java                                                                  
//----------------------------------------------------------------------------

//## package Default 


//## class ReadyController 
public class ReadyController implements RiJStateConcept {
    
    public Reactive reactive;		//## ignore 
    
    protected int gotReady;		//## attribute gotReady 
    
    protected Elevator el;		//## link el 
    
    //#[ ignore 
    public static final int RiJNonState=0;
    public static final int Init=1;
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
    public  ReadyController(RiJThread p_thread) {
        reactive = new Reactive(p_thread);
    }
    
    //## auto_generated 
    public int getGotReady() {
        return gotReady;
    }
    
    //## auto_generated 
    public void setGotReady(int p_gotReady) {
        gotReady = p_gotReady;
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
                el.__setRc(null);
            }
        __setEl(p_Elevator);
    }
    
    //## auto_generated 
    public void setEl(Elevator p_Elevator) {
        if(p_Elevator != null)
            {
                p_Elevator._setRc(this);
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
            if(rootState_active == Init)
                {
                    res = Init_takeEvent(id);
                }
            return res;
        }
        
        //## auto_generated 
        protected void initStatechart() {
            rootState_subState = RiJNonState;
            rootState_active = RiJNonState;
        }
        
        //## statechart_method 
        public void InitEnter() {
        }
        
        //## statechart_method 
        public int InitTakeReady() {
            Ready params = (Ready) event;
            int res = RiJStateReactive.TAKE_EVENT_NOT_CONSUMED;
            //#[ transition 1 
            if(el.hc.getLevel() == params.level) {
            	el.gen(new ReadyControllerE());
            }
            //#]
            res = RiJStateReactive.TAKE_EVENT_COMPLETE;
            return res;
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
        public int rootState_takeEvent(short id) {
            int res = RiJStateReactive.TAKE_EVENT_NOT_CONSUMED;
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
        public void rootStateEntDef() {
            Init_entDef();
        }
        
        //## statechart_method 
        public void Init_enter() {
            rootState_subState = Init;
            rootState_active = Init;
            InitEnter();
        }
        
        //## statechart_method 
        public void rootStateExit() {
        }
        
        //## statechart_method 
        public void InitExit() {
        }
        
        //## statechart_method 
        public int Init_takeEvent(short id) {
            int res = RiJStateReactive.TAKE_EVENT_NOT_CONSUMED;
            if(event.isTypeOf(Ready.Ready_Default_id))
                {
                    res = InitTakeReady();
                }
            
            return res;
        }
        
    }
}
/*********************************************************************
	File Path	: exe/DefaultConfig/Default/ReadyController.java
*********************************************************************/

