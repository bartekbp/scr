I-Logix-RPY-Archive version 8.8.0 Java 6107223
{ IProject 
	- _id = GUID 0c8283b7-8ceb-4ff1-b6c8-24b29e07e251;
	- _myState = 8192;
	- _name = "Elevator";
	- _modifiedTimeWeak = 11.17.2013::14:54:1;
	- _lastID = 1;
	- _UserColors = { IRPYRawContainer 
		- size = 16;
		- value = 16777215; 16777215; 16777215; 16777215; 16777215; 16777215; 16777215; 16777215; 16777215; 16777215; 16777215; 16777215; 16777215; 16777215; 16777215; 16777215; 
	}
	- _defaultSubsystem = { ISubsystemHandle 
		- _m2Class = "ISubsystem";
		- _filename = "Default.sbs";
		- _subsystem = "";
		- _class = "";
		- _name = "Default";
		- _id = GUID 2970263e-bdf6-4006-ba3e-12cef9acae52;
	}
	- _component = { IHandle 
		- _m2Class = "IComponent";
		- _filename = "animator.cmp";
		- _subsystem = "";
		- _class = "";
		- _name = "animator";
		- _id = GUID a20b32e6-7af9-4318-b013-27301c21bdda;
	}
	- Multiplicities = { IRPYRawContainer 
		- size = 5;
		- value = 
		{ IMultiplicityItem 
			- _name = "1";
			- _count = 8;
		}
		{ IMultiplicityItem 
			- _name = "*";
			- _count = -1;
		}
		{ IMultiplicityItem 
			- _name = "0,1";
			- _count = -1;
		}
		{ IMultiplicityItem 
			- _name = "1..*";
			- _count = -1;
		}
		{ IMultiplicityItem 
			- _name = "4";
			- _count = 0;
		}
	}
	- Subsystems = { IRPYRawContainer 
		- size = 7;
		- value = 
		{ ISubsystem 
			- fileName = "Default";
			- _id = GUID 2970263e-bdf6-4006-ba3e-12cef9acae52;
		}
		{ IProfile 
			- fileName = "JavaDocProfile";
			- _persistAs = "$OMROOT\\Profiles\\JavaDoc";
			- _id = GUID 19700e28-456f-4c97-a19c-b95dcb3e9dff;
			- _isReference = 1;
		}
		{ IProfile 
			- fileName = "Pre76GESkin";
			- _id = GUID 74a6daed-8619-4275-8f6b-7d1d1d0220b1;
		}
		{ IProfile 
			- fileName = "CGCompatibilityPre753Java";
			- _id = GUID 1a373eb2-7fe0-464e-80c5-32bbc6b2649c;
		}
		{ IProfile 
			- fileName = "CGCompatibilityPre761Java";
			- _id = GUID 2f79df25-5e16-4a5a-876b-4528cded0c3d;
		}
		{ IProfile 
			- fileName = "CGCompatibilityPre80Java";
			- _id = GUID 8d3592d4-30e4-4723-9947-9c46c2a3bc85;
		}
		{ IProfile 
			- fileName = "CGCompatibilityPre803Java";
			- _id = GUID 3b75956f-f2d2-4ee0-b54e-32b7891132aa;
		}
	}
	- Diagrams = { IRPYRawContainer 
		- size = 0;
	}
	- MSCS = { IRPYRawContainer 
		- size = 0;
	}
	- Components = { IRPYRawContainer 
		- size = 2;
		- value = 
		{ IComponent 
			- fileName = "animator";
			- _id = GUID a20b32e6-7af9-4318-b013-27301c21bdda;
		}
		{ IComponent 
			- fileName = "exe";
			- _id = GUID d90e55dd-0cab-4770-8e09-c67348fe3912;
		}
	}
}

