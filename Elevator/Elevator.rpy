I-Logix-RPY-Archive version 8.8.0 Java 6107223
{ IProject 
	- _id = GUID 0c8283b7-8ceb-4ff1-b6c8-24b29e07e251;
	- _myState = 8192;
	- _name = "Elevator";
	- _modifiedTimeWeak = 11.29.2013::8:52:52;
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
		- size = 3;
		- value = 
		{ IMSC 
			- _id = GUID b9a86ee9-46fa-4734-80b6-f7bcd0082c93;
			- _myState = 8192;
			- _properties = { IPropertyContainer 
				- Subjects = { IRPYRawContainer 
					- size = 1;
					- value = 
					{ IPropertySubject 
						- _Name = "Format";
						- Metaclasses = { IRPYRawContainer 
							- size = 3;
							- value = 
							{ IPropertyMetaclass 
								- _Name = "Condition_Mark";
								- Properties = { IRPYRawContainer 
									- size = 8;
									- value = 
									{ IProperty 
										- _Name = "DefaultSize";
										- _Value = "0,0,67,39";
										- _Type = String;
									}
									{ IProperty 
										- _Name = "Fill.FillColor";
										- _Value = "255,255,255";
										- _Type = Color;
									}
									{ IProperty 
										- _Name = "Font.Font";
										- _Value = "Arial";
										- _Type = String;
									}
									{ IProperty 
										- _Name = "Font.FontColor";
										- _Value = "0,0,0";
										- _Type = Color;
									}
									{ IProperty 
										- _Name = "Font.Size";
										- _Value = "10";
										- _Type = Int;
									}
									{ IProperty 
										- _Name = "Font.Weight@Child.NameCompartment@Name";
										- _Value = "$<cancel>";
										- _Type = Int;
									}
									{ IProperty 
										- _Name = "Line.LineColor";
										- _Value = "0,112,0";
										- _Type = Color;
									}
									{ IProperty 
										- _Name = "Line.LineWidth";
										- _Value = "1";
										- _Type = Int;
									}
								}
							}
							{ IPropertyMetaclass 
								- _Name = "InstanceLine";
								- Properties = { IRPYRawContainer 
									- size = 8;
									- value = 
									{ IProperty 
										- _Name = "DefaultSize";
										- _Value = "0,0,96,437";
										- _Type = String;
									}
									{ IProperty 
										- _Name = "Fill.FillColor";
										- _Value = "255,255,255";
										- _Type = Color;
									}
									{ IProperty 
										- _Name = "Font.Font";
										- _Value = "Arial";
										- _Type = String;
									}
									{ IProperty 
										- _Name = "Font.FontColor";
										- _Value = "0,0,0";
										- _Type = Color;
									}
									{ IProperty 
										- _Name = "Font.Size";
										- _Value = "10";
										- _Type = Int;
									}
									{ IProperty 
										- _Name = "Font.Weight@Child.NameCompartment@Name";
										- _Value = "$<cancel>";
										- _Type = Int;
									}
									{ IProperty 
										- _Name = "Line.LineColor";
										- _Value = "121,122,0";
										- _Type = Color;
									}
									{ IProperty 
										- _Name = "Line.LineWidth";
										- _Value = "0";
										- _Type = Int;
									}
								}
							}
							{ IPropertyMetaclass 
								- _Name = "Message";
								- Properties = { IRPYRawContainer 
									- size = 5;
									- value = 
									{ IProperty 
										- _Name = "Font.Font";
										- _Value = "Arial";
										- _Type = String;
									}
									{ IProperty 
										- _Name = "Font.FontColor";
										- _Value = "0,0,128";
										- _Type = Color;
									}
									{ IProperty 
										- _Name = "Font.Size";
										- _Value = "10";
										- _Type = Int;
									}
									{ IProperty 
										- _Name = "Line.LineColor";
										- _Value = "0,112,0";
										- _Type = Color;
									}
									{ IProperty 
										- _Name = "Line.LineWidth";
										- _Value = "1";
										- _Type = Int;
									}
								}
							}
						}
					}
				}
			}
			- _name = "f";
			- _modifiedTimeWeak = 1.2.1990::0:0:0;
			- _lastModifiedTime = "11.19.2013::20:18:5";
			- _graphicChart = { CGIMscChart 
				- vLadderMargin = 20;
				- m_usingActivationBar = 0;
				- _id = GUID dca21262-8871-42cf-a05a-9f42f958c968;
				- m_type = 0;
				- m_pModelObject = { IHandle 
					- _m2Class = "IMSC";
					- _id = GUID b9a86ee9-46fa-4734-80b6-f7bcd0082c93;
				}
				- m_pParent = ;
				- m_name = { CGIText 
					- m_str = "";
					- m_style = "Arial" 10 0 0 0 1 ;
					- m_color = { IColor 
						- m_fgColor = 0;
						- m_bgColor = 0;
						- m_bgFlag = 0;
					}
					- m_position = 1 0 0  ;
					- m_nIdent = 0;
					- m_bImplicitSetRectPoints = 0;
					- m_nOrientationCtrlPt = 8;
				}
				- m_drawBehavior = 0;
				- m_bIsPreferencesInitialized = 0;
				- elementList = 14;
				{ CGIBox 
					- _id = GUID 1e92d4f9-07d4-40a9-97cc-23fe15c69fa1;
					- m_type = 108;
					- m_pModelObject = { IHandle 
						- _m2Class = "ICollaboration";
						- _id = GUID aa4e397d-4c19-4f5b-8d9c-3f3e95412eca;
					}
					- m_pParent = ;
					- m_name = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_drawBehavior = 0;
					- m_bIsPreferencesInitialized = 0;
					- m_polygon = 0 ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
					- Compartments = { IRPYRawContainer 
						- size = 0;
					}
				}
				{ CGIMscColumnCR 
					- _id = GUID fb42f520-606e-4c25-9bbd-4c3acc501571;
					- m_type = 109;
					- m_pModelObject = { IHandle 
						- _m2Class = "IClassifierRole";
						- _id = GUID 0a699d65-0a7c-49c9-8ec4-d44fcef233e4;
					}
					- m_pParent = GUID 1e92d4f9-07d4-40a9-97cc-23fe15c69fa1;
					- m_name = { CGIText 
						- m_str = "Elevator[0]:Elevator";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_drawBehavior = 0;
					- m_transform = 1 0 0 0.0164378 181 50 ;
					- m_bIsPreferencesInitialized = 1;
					- m_AdditionalLabel = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 1;
					}
					- m_position = 4 0 0  0 49885  96 49885  96 0  ;
					- m_pInheritsFrom = { IHandle 
						- _m2Class = "";
					}
					- m_nInheritanceMask = 0;
					- m_SubType = 0;
				}
				{ CGIMscColumnCR 
					- _id = GUID 11e2ab5d-500f-407c-b674-92f017412c8a;
					- m_type = 109;
					- m_pModelObject = { IHandle 
						- _m2Class = "IClassifierRole";
						- _id = GUID a8dfc413-d4b2-437c-99b6-e9773e0586a3;
					}
					- m_pParent = GUID 1e92d4f9-07d4-40a9-97cc-23fe15c69fa1;
					- m_name = { CGIText 
						- m_str = "Elevator[0]->dc:DoorsController";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_drawBehavior = 0;
					- m_transform = 1 0 0 0.0164378 363 50 ;
					- m_bIsPreferencesInitialized = 1;
					- m_AdditionalLabel = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 1;
					}
					- m_position = 4 0 0  0 49885  96 49885  96 0  ;
					- m_pInheritsFrom = { IHandle 
						- _m2Class = "";
					}
					- m_nInheritanceMask = 0;
					- m_SubType = 0;
				}
				{ CGIMscColumnCR 
					- _id = GUID 9f0307a5-d8ad-414e-9e94-ad3e415101fe;
					- m_type = 109;
					- m_pModelObject = { IHandle 
						- _m2Class = "IClassifierRole";
						- _id = GUID b9e6286f-c13c-45c3-b45f-6594924f8939;
					}
					- m_pParent = GUID 1e92d4f9-07d4-40a9-97cc-23fe15c69fa1;
					- m_name = { CGIText 
						- m_str = "Elevator[0]->dh:DoorsOpenedHandler";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_drawBehavior = 0;
					- m_transform = 1 0 0 0.0164378 675 50 ;
					- m_bIsPreferencesInitialized = 1;
					- m_AdditionalLabel = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 1;
					}
					- m_position = 4 0 0  0 49885  96 49885  96 0  ;
					- m_pInheritsFrom = { IHandle 
						- _m2Class = "";
					}
					- m_nInheritanceMask = 0;
					- m_SubType = 0;
				}
				{ CGIMscColumnCR 
					- _id = GUID 4b3cd0c1-8c3c-495a-903d-e92c3e4d9aff;
					- m_type = 109;
					- m_pModelObject = { IHandle 
						- _m2Class = "IClassifierRole";
						- _id = GUID c17b7779-3b6a-40cb-9c45-e4f587f5ef40;
					}
					- m_pParent = GUID 1e92d4f9-07d4-40a9-97cc-23fe15c69fa1;
					- m_name = { CGIText 
						- m_str = "Elevator[0]->fl[0]:Floor";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_drawBehavior = 0;
					- m_transform = 1 0 0 0.0164378 502 50 ;
					- m_bIsPreferencesInitialized = 1;
					- m_AdditionalLabel = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 1;
					}
					- m_position = 4 0 0  0 49885  96 49885  96 0  ;
					- m_pInheritsFrom = { IHandle 
						- _m2Class = "";
					}
					- m_nInheritanceMask = 0;
					- m_SubType = 0;
				}
				{ CGIMscConditionMark 
					- _id = GUID 3d8582e0-8c34-4ed2-88e7-6d7393e0f9a6;
					- _properties = { IPropertyContainer 
						- Subjects = { IRPYRawContainer 
							- size = 1;
							- value = 
							{ IPropertySubject 
								- _Name = "SequenceDiagram";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "Condition_Mark";
										- Properties = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IProperty 
												- _Name = "AlignConditionMarksLeft";
												- _Value = "True";
												- _Type = Bool;
											}
										}
									}
								}
							}
						}
					}
					- m_type = 114;
					- m_pModelObject = { IHandle 
						- _m2Class = "IMessage";
						- _id = GUID 475eda4f-1f8b-4676-994d-9929d58b956b;
					}
					- m_pParent = GUID 9f0307a5-d8ad-414e-9e94-ad3e415101fe;
					- m_name = { CGIText 
						- m_str = "handle";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_drawBehavior = 4096;
					- m_transform = 1.14286 0 0 60.8354 0 8213 ;
					- m_bIsPreferencesInitialized = 1;
					- m_polygon = 4 0 0  0 51  84 51  84 0  ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
					- Compartments = { IRPYRawContainer 
						- size = 0;
					}
				}
				{ CGIMscConditionMark 
					- _id = GUID 32a96de4-c99e-44f1-9c7f-177b81ba9459;
					- _properties = { IPropertyContainer 
						- Subjects = { IRPYRawContainer 
							- size = 1;
							- value = 
							{ IPropertySubject 
								- _Name = "SequenceDiagram";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "Condition_Mark";
										- Properties = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IProperty 
												- _Name = "AlignConditionMarksLeft";
												- _Value = "True";
												- _Type = Bool;
											}
										}
									}
								}
							}
						}
					}
					- m_type = 114;
					- m_pModelObject = { IHandle 
						- _m2Class = "IMessage";
						- _id = GUID 72ec30a0-f9e6-4245-8b02-ef5d6f981894;
					}
					- m_pParent = GUID 11e2ab5d-500f-407c-b674-92f017412c8a;
					- m_name = { CGIText 
						- m_str = "Waiting";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_drawBehavior = 4096;
					- m_transform = 1.14286 0 0 60.8354 0 3893 ;
					- m_bIsPreferencesInitialized = 1;
					- m_polygon = 4 0 0  0 51  84 51  84 0  ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
					- Compartments = { IRPYRawContainer 
						- size = 0;
					}
				}
				{ CGIMscConditionMark 
					- _id = GUID c353f95b-6cce-44f3-b7d6-a8efecb522f5;
					- _properties = { IPropertyContainer 
						- Subjects = { IRPYRawContainer 
							- size = 1;
							- value = 
							{ IPropertySubject 
								- _Name = "SequenceDiagram";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "Condition_Mark";
										- Properties = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IProperty 
												- _Name = "AlignConditionMarksLeft";
												- _Value = "True";
												- _Type = Bool;
											}
										}
									}
								}
							}
						}
					}
					- m_type = 114;
					- m_pModelObject = { IHandle 
						- _m2Class = "IMessage";
						- _id = GUID 7f3a1db8-6eec-4dee-ad77-5df73c8293d6;
					}
					- m_pParent = GUID fb42f520-606e-4c25-9bbd-4c3acc501571;
					- m_name = { CGIText 
						- m_str = "Stopped";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_drawBehavior = 4096;
					- m_transform = 1.14286 0 0 60.8354 0 33642 ;
					- m_bIsPreferencesInitialized = 1;
					- m_polygon = 4 0 0  0 51  84 51  84 0  ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
					- Compartments = { IRPYRawContainer 
						- size = 0;
					}
				}
				{ CGIMscConditionMark 
					- _id = GUID 0c390db1-9fe5-433e-a82f-7377c38869a7;
					- _properties = { IPropertyContainer 
						- Subjects = { IRPYRawContainer 
							- size = 1;
							- value = 
							{ IPropertySubject 
								- _Name = "SequenceDiagram";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "Condition_Mark";
										- Properties = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IProperty 
												- _Name = "AlignConditionMarksLeft";
												- _Value = "True";
												- _Type = Bool;
											}
										}
									}
								}
							}
						}
					}
					- m_type = 114;
					- m_pModelObject = { IHandle 
						- _m2Class = "IMessage";
						- _id = GUID 598f99a9-6dd8-4692-aca7-96a6001bd39b;
					}
					- m_pParent = GUID fb42f520-606e-4c25-9bbd-4c3acc501571;
					- m_name = { CGIText 
						- m_str = "EmergencyStopped";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_drawBehavior = 4096;
					- m_transform = 1.14286 0 0 93.0423 0 17399 ;
					- m_bIsPreferencesInitialized = 1;
					- m_polygon = 4 0 0  0 51  84 51  84 0  ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
					- Compartments = { IRPYRawContainer 
						- size = 0;
					}
				}
				{ CGIMscConditionMark 
					- _id = GUID ae57b0ae-1e05-44fc-80f1-803a964d2c48;
					- _properties = { IPropertyContainer 
						- Subjects = { IRPYRawContainer 
							- size = 1;
							- value = 
							{ IPropertySubject 
								- _Name = "SequenceDiagram";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "Condition_Mark";
										- Properties = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IProperty 
												- _Name = "AlignConditionMarksLeft";
												- _Value = "True";
												- _Type = Bool;
											}
										}
									}
								}
							}
						}
					}
					- m_type = 114;
					- m_pModelObject = { IHandle 
						- _m2Class = "IMessage";
						- _id = GUID 07ea118e-21b1-4928-9824-3336a4611a10;
					}
					- m_pParent = GUID fb42f520-606e-4c25-9bbd-4c3acc501571;
					- m_name = { CGIText 
						- m_str = "waitingForRequest";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_drawBehavior = 4096;
					- m_transform = 1.14286 0 0 93.0423 0 23361 ;
					- m_bIsPreferencesInitialized = 1;
					- m_polygon = 4 0 0  0 51  84 51  84 0  ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
					- Compartments = { IRPYRawContainer 
						- size = 0;
					}
				}
				{ CGIMscConditionMark 
					- _id = GUID 1d067a98-bad3-49de-b8a3-850702c05721;
					- _properties = { IPropertyContainer 
						- Subjects = { IRPYRawContainer 
							- size = 1;
							- value = 
							{ IPropertySubject 
								- _Name = "SequenceDiagram";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "Condition_Mark";
										- Properties = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IProperty 
												- _Name = "AlignConditionMarksLeft";
												- _Value = "True";
												- _Type = Bool;
											}
										}
									}
								}
							}
						}
					}
					- m_type = 114;
					- m_pModelObject = { IHandle 
						- _m2Class = "IMessage";
						- _id = GUID c9726350-c3ca-4f85-b5eb-44fdc32b4b9b;
					}
					- m_pParent = GUID fb42f520-606e-4c25-9bbd-4c3acc501571;
					- m_name = { CGIText 
						- m_str = "Moving";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_drawBehavior = 4096;
					- m_transform = 1.14286 0 0 60.8354 0 29323 ;
					- m_bIsPreferencesInitialized = 1;
					- m_polygon = 4 0 0  0 51  84 51  84 0  ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
					- Compartments = { IRPYRawContainer 
						- size = 0;
					}
				}
				{ CGIMscMessage 
					- _id = GUID 2c8bb6a2-6db4-4c38-91cb-1b459002112d;
					- _properties = { IPropertyContainer 
						- Subjects = { IRPYRawContainer 
							- size = 1;
							- value = 
							{ IPropertySubject 
								- _Name = "Format";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "Message";
										- Properties = { IRPYRawContainer 
											- size = 2;
											- value = 
											{ IProperty 
												- _Name = "Line.LineStyle";
												- _Value = "0";
												- _Type = Int;
											}
											{ IProperty 
												- _Name = "Line.LineWidth";
												- _Value = "1";
												- _Type = Int;
											}
										}
									}
								}
							}
						}
					}
					- m_type = 110;
					- m_pModelObject = { IHandle 
						- _m2Class = "IMessage";
						- _id = GUID 76e6eb97-e22e-44f0-8764-08cdf975090f;
					}
					- m_pParent = ;
					- m_name = { CGIText 
						- m_str = "DoorsOpened(level = 1, areOpened = true)";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 4;
					}
					- m_drawBehavior = 4096;
					- m_bIsPreferencesInitialized = 1;
					- m_pSource = GUID 11e2ab5d-500f-407c-b674-92f017412c8a;
					- m_sourceType = 'F';
					- m_pTarget = GUID fb42f520-606e-4c25-9bbd-4c3acc501571;
					- m_targetType = 'T';
					- m_direction = ' ';
					- m_rpn = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_anglePoint1 = 0 0 ;
					- m_anglePoint2 = 0 0 ;
					- m_line_style = 0;
					- m_SourcePort = 48 15331 ;
					- m_TargetPort = 48 16547 ;
					- m_bLeft = 0;
				}
				{ CGIMscMessage 
					- _id = GUID ec75e213-3193-46dd-ad28-c08bfacc2ae3;
					- _properties = { IPropertyContainer 
						- Subjects = { IRPYRawContainer 
							- size = 1;
							- value = 
							{ IPropertySubject 
								- _Name = "Format";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "Message";
										- Properties = { IRPYRawContainer 
											- size = 2;
											- value = 
											{ IProperty 
												- _Name = "Line.LineStyle";
												- _Value = "0";
												- _Type = Int;
											}
											{ IProperty 
												- _Name = "Line.LineWidth";
												- _Value = "1";
												- _Type = Int;
											}
										}
									}
								}
							}
						}
					}
					- m_type = 110;
					- m_pModelObject = { IHandle 
						- _m2Class = "IMessage";
						- _id = GUID 1b22ff79-6e2d-4855-b679-c0dff9dcbea5;
					}
					- m_pParent = ;
					- m_name = { CGIText 
						- m_str = "DoorsOpenedController(areOpened = false)";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 4;
					}
					- m_drawBehavior = 4096;
					- m_bIsPreferencesInitialized = 1;
					- m_pSource = GUID 11e2ab5d-500f-407c-b674-92f017412c8a;
					- m_sourceType = 'F';
					- m_pTarget = GUID fb42f520-606e-4c25-9bbd-4c3acc501571;
					- m_targetType = 'T';
					- m_direction = ' ';
					- m_rpn = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_anglePoint1 = 0 0 ;
					- m_anglePoint2 = 0 0 ;
					- m_line_style = 0;
					- m_SourcePort = 48 12897 ;
					- m_TargetPort = 48 14114 ;
					- m_bLeft = 0;
				}
				{ CGIMscMessage 
					- _id = GUID 2f930e3c-5bcd-4a81-8f80-cdd6443d7b0d;
					- _properties = { IPropertyContainer 
						- Subjects = { IRPYRawContainer 
							- size = 1;
							- value = 
							{ IPropertySubject 
								- _Name = "Format";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "Message";
										- Properties = { IRPYRawContainer 
											- size = 2;
											- value = 
											{ IProperty 
												- _Name = "Line.LineStyle";
												- _Value = "0";
												- _Type = Int;
											}
											{ IProperty 
												- _Name = "Line.LineWidth";
												- _Value = "1";
												- _Type = Int;
											}
										}
									}
								}
							}
						}
					}
					- m_type = 110;
					- m_pModelObject = { IHandle 
						- _m2Class = "IMessage";
						- _id = GUID c2e5b8d8-2bd4-4184-a8c2-9be6d315d1a9;
					}
					- m_pParent = ;
					- m_name = { CGIText 
						- m_str = "DoorsOpenedController(areOpened = true)";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 4;
					}
					- m_drawBehavior = 4096;
					- m_bIsPreferencesInitialized = 1;
					- m_pSource = GUID 11e2ab5d-500f-407c-b674-92f017412c8a;
					- m_sourceType = 'F';
					- m_pTarget = GUID fb42f520-606e-4c25-9bbd-4c3acc501571;
					- m_targetType = 'T';
					- m_direction = ' ';
					- m_rpn = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_anglePoint1 = 0 0 ;
					- m_anglePoint2 = 0 0 ;
					- m_line_style = 0;
					- m_SourcePort = 48 38326 ;
					- m_TargetPort = 48 39543 ;
					- m_bLeft = 0;
				}
				
				- m_access = 'Z';
				- m_modified = 'N';
				- m_fileVersion = "";
				- m_nModifyDate = 0;
				- m_nCreateDate = 0;
				- m_creator = "";
				- m_bScaleWithZoom = 1;
				- m_arrowStyle = 'S';
				- m_pRoot = GUID 1e92d4f9-07d4-40a9-97cc-23fe15c69fa1;
				- m_currentLeftTop = 0 0 ;
				- m_currentRightBottom = 0 0 ;
			}
			- _defaultSubsystem = { IHandle 
				- _m2Class = "ISubsystem";
				- _filename = "Default.sbs";
				- _subsystem = "";
				- _class = "";
				- _name = "Default";
				- _id = GUID 2970263e-bdf6-4006-ba3e-12cef9acae52;
			}
			- m_pICollaboration = { ICollaboration 
				- _id = GUID aa4e397d-4c19-4f5b-8d9c-3f3e95412eca;
				- _modifiedTimeWeak = 1.2.1990::0:0:0;
				- ClassifierRoles = { IRPYRawContainer 
					- size = 4;
					- value = 
					{ IClassifierRole 
						- _id = GUID 0a699d65-0a7c-49c9-8ec4-d44fcef233e4;
						- _name = "Elevator[0]";
						- _modifiedTimeWeak = 1.2.1990::0:0:0;
						- m_eRoleType = CLASS;
						- m_pBase = { IHandle 
							- _m2Class = "IClass";
							- _filename = "Default.sbs";
							- _subsystem = "Default";
							- _class = "";
							- _name = "Elevator";
							- _id = GUID 6e9ca01c-040b-4e85-bbc9-4f7798db5ef4;
						}
						- m_instance = { IHandle 
							- _m2Class = "";
						}
					}
					{ IClassifierRole 
						- _id = GUID a8dfc413-d4b2-437c-99b6-e9773e0586a3;
						- _name = "Elevator[0]->dc";
						- _modifiedTimeWeak = 1.2.1990::0:0:0;
						- m_eRoleType = CLASS;
						- m_pBase = { IHandle 
							- _m2Class = "IClass";
							- _filename = "Default.sbs";
							- _subsystem = "Default";
							- _class = "";
							- _name = "DoorsController";
							- _id = GUID 38aec46c-a896-46bc-bad4-16c77e5569d0;
						}
						- m_instance = { IHandle 
							- _m2Class = "";
						}
					}
					{ IClassifierRole 
						- _id = GUID b9e6286f-c13c-45c3-b45f-6594924f8939;
						- _name = "Elevator[0]->dh";
						- _modifiedTimeWeak = 1.2.1990::0:0:0;
						- m_eRoleType = CLASS;
						- m_pBase = { IHandle 
							- _m2Class = "IClass";
							- _filename = "Default.sbs";
							- _subsystem = "Default";
							- _class = "";
							- _name = "DoorsOpenedHandler";
							- _id = GUID e5c8bcb2-d1fa-4e71-af13-4292f7a7b62a;
						}
						- m_instance = { IHandle 
							- _m2Class = "";
						}
					}
					{ IClassifierRole 
						- _id = GUID c17b7779-3b6a-40cb-9c45-e4f587f5ef40;
						- _name = "Elevator[0]->fl[0]";
						- _modifiedTimeWeak = 1.2.1990::0:0:0;
						- m_eRoleType = CLASS;
						- m_pBase = { IHandle 
							- _m2Class = "IClass";
							- _filename = "Default.sbs";
							- _subsystem = "Default";
							- _class = "";
							- _name = "Floor";
							- _id = GUID 7270c741-82dd-4d79-a637-77a3d1fb86d5;
						}
						- m_instance = { IHandle 
							- _m2Class = "";
						}
					}
				}
				- Messages = { IRPYRawContainer 
					- size = 9;
					- value = 
					{ IMessage 
						- _id = GUID 72ec30a0-f9e6-4245-8b02-ef5d6f981894;
						- _properties = { IPropertyContainer 
							- Subjects = { IRPYRawContainer 
								- size = 1;
								- value = 
								{ IPropertySubject 
									- _Name = "SequenceDiagram";
									- Metaclasses = { IRPYRawContainer 
										- size = 1;
										- value = 
										{ IPropertyMetaclass 
											- _Name = "Condition_Mark";
											- Properties = { IRPYRawContainer 
												- size = 1;
												- value = 
												{ IProperty 
													- _Name = "IsStateCondition";
													- _Value = "True";
													- _Type = Bool;
												}
											}
										}
									}
								}
							}
						}
						- _name = "connector";
						- _modifiedTimeWeak = 1.2.1990::0:0:0;
						- m_szSequence = "";
						- m_szActualArgs = "";
						- m_szReturnVal = "";
						- m_freeText = "Waiting";
						- m_pCommunicationConnection = { IHandle 
							- _m2Class = "";
						}
						- m_pReceiver = { IHandle 
							- _m2Class = "IClassifierRole";
							- _id = GUID a8dfc413-d4b2-437c-99b6-e9773e0586a3;
						}
						- m_pSender = { IHandle 
							- _m2Class = "IClassifierRole";
							- _id = GUID a8dfc413-d4b2-437c-99b6-e9773e0586a3;
						}
						- m_pFormalMessage = { IHandle 
							- _m2Class = "";
						}
						- m_eType = CONDITION;
						- m_targetExec = { IHandle 
							- _m2Class = "";
						}
						- m_srcExec = { IHandle 
							- _m2Class = "";
						}
					}
					{ IMessage 
						- _id = GUID 475eda4f-1f8b-4676-994d-9929d58b956b;
						- _properties = { IPropertyContainer 
							- Subjects = { IRPYRawContainer 
								- size = 1;
								- value = 
								{ IPropertySubject 
									- _Name = "SequenceDiagram";
									- Metaclasses = { IRPYRawContainer 
										- size = 1;
										- value = 
										{ IPropertyMetaclass 
											- _Name = "Condition_Mark";
											- Properties = { IRPYRawContainer 
												- size = 1;
												- value = 
												{ IProperty 
													- _Name = "IsStateCondition";
													- _Value = "True";
													- _Type = Bool;
												}
											}
										}
									}
								}
							}
						}
						- _name = "connector";
						- _modifiedTimeWeak = 1.2.1990::0:0:0;
						- m_szSequence = "";
						- m_szActualArgs = "";
						- m_szReturnVal = "";
						- m_freeText = "handle";
						- m_pCommunicationConnection = { IHandle 
							- _m2Class = "";
						}
						- m_pReceiver = { IHandle 
							- _m2Class = "IClassifierRole";
							- _id = GUID b9e6286f-c13c-45c3-b45f-6594924f8939;
						}
						- m_pSender = { IHandle 
							- _m2Class = "IClassifierRole";
							- _id = GUID b9e6286f-c13c-45c3-b45f-6594924f8939;
						}
						- m_pFormalMessage = { IHandle 
							- _m2Class = "";
						}
						- m_eType = CONDITION;
						- m_targetExec = { IHandle 
							- _m2Class = "";
						}
						- m_srcExec = { IHandle 
							- _m2Class = "";
						}
					}
					{ IMessage 
						- _id = GUID 1b22ff79-6e2d-4855-b679-c0dff9dcbea5;
						- _myState = 8192;
						- _name = "DoorsOpenedController";
						- _modifiedTimeWeak = 1.2.1990::0:0:0;
						- m_szSequence = "1.";
						- m_szActualArgs = "areOpened = false";
						- m_szReturnVal = "";
						- m_pCommunicationConnection = { IHandle 
							- _m2Class = "";
						}
						- m_pReceiver = { IHandle 
							- _m2Class = "IClassifierRole";
							- _id = GUID 0a699d65-0a7c-49c9-8ec4-d44fcef233e4;
						}
						- m_pSender = { IHandle 
							- _m2Class = "IClassifierRole";
							- _id = GUID a8dfc413-d4b2-437c-99b6-e9773e0586a3;
						}
						- m_pFormalMessage = { IHandle 
							- _m2Class = "IEvent";
							- _filename = "Default.sbs";
							- _subsystem = "Default";
							- _class = "";
							- _name = "DoorsOpenedController(boolean)";
							- _id = GUID 8d9584ef-b0bf-4119-af91-fb0310eb32e2;
						}
						- m_eType = EVENT;
						- m_targetExec = { IHandle 
							- _m2Class = "";
						}
						- m_srcExec = { IHandle 
							- _m2Class = "";
						}
					}
					{ IMessage 
						- _id = GUID 76e6eb97-e22e-44f0-8764-08cdf975090f;
						- _myState = 8192;
						- _name = "DoorsOpened";
						- _modifiedTimeWeak = 1.2.1990::0:0:0;
						- m_szSequence = "2.";
						- m_szActualArgs = "level = 1, areOpened = true";
						- m_szReturnVal = "";
						- m_pCommunicationConnection = { IHandle 
							- _m2Class = "";
						}
						- m_pReceiver = { IHandle 
							- _m2Class = "IClassifierRole";
							- _id = GUID 0a699d65-0a7c-49c9-8ec4-d44fcef233e4;
						}
						- m_pSender = { IHandle 
							- _m2Class = "IClassifierRole";
							- _id = GUID a8dfc413-d4b2-437c-99b6-e9773e0586a3;
						}
						- m_pFormalMessage = { IHandle 
							- _m2Class = "IEvent";
							- _filename = "Default.sbs";
							- _subsystem = "Default";
							- _class = "";
							- _name = "DoorsOpened(int,boolean)";
							- _id = GUID 2a78ba89-6080-4011-930a-25332c7a1a67;
						}
						- m_eType = EVENT;
						- m_targetExec = { IHandle 
							- _m2Class = "";
						}
						- m_srcExec = { IHandle 
							- _m2Class = "";
						}
					}
					{ IMessage 
						- _id = GUID 598f99a9-6dd8-4692-aca7-96a6001bd39b;
						- _properties = { IPropertyContainer 
							- Subjects = { IRPYRawContainer 
								- size = 1;
								- value = 
								{ IPropertySubject 
									- _Name = "SequenceDiagram";
									- Metaclasses = { IRPYRawContainer 
										- size = 1;
										- value = 
										{ IPropertyMetaclass 
											- _Name = "Condition_Mark";
											- Properties = { IRPYRawContainer 
												- size = 1;
												- value = 
												{ IProperty 
													- _Name = "IsStateCondition";
													- _Value = "True";
													- _Type = Bool;
												}
											}
										}
									}
								}
							}
						}
						- _name = "connector";
						- _modifiedTimeWeak = 1.2.1990::0:0:0;
						- m_szSequence = "";
						- m_szActualArgs = "";
						- m_szReturnVal = "";
						- m_freeText = "EmergencyStopped";
						- m_pCommunicationConnection = { IHandle 
							- _m2Class = "";
						}
						- m_pReceiver = { IHandle 
							- _m2Class = "IClassifierRole";
							- _id = GUID 0a699d65-0a7c-49c9-8ec4-d44fcef233e4;
						}
						- m_pSender = { IHandle 
							- _m2Class = "IClassifierRole";
							- _id = GUID 0a699d65-0a7c-49c9-8ec4-d44fcef233e4;
						}
						- m_pFormalMessage = { IHandle 
							- _m2Class = "";
						}
						- m_eType = CONDITION;
						- m_targetExec = { IHandle 
							- _m2Class = "";
						}
						- m_srcExec = { IHandle 
							- _m2Class = "";
						}
					}
					{ IMessage 
						- _id = GUID 07ea118e-21b1-4928-9824-3336a4611a10;
						- _properties = { IPropertyContainer 
							- Subjects = { IRPYRawContainer 
								- size = 1;
								- value = 
								{ IPropertySubject 
									- _Name = "SequenceDiagram";
									- Metaclasses = { IRPYRawContainer 
										- size = 1;
										- value = 
										{ IPropertyMetaclass 
											- _Name = "Condition_Mark";
											- Properties = { IRPYRawContainer 
												- size = 1;
												- value = 
												{ IProperty 
													- _Name = "IsStateCondition";
													- _Value = "True";
													- _Type = Bool;
												}
											}
										}
									}
								}
							}
						}
						- _name = "connector";
						- _modifiedTimeWeak = 1.2.1990::0:0:0;
						- m_szSequence = "";
						- m_szActualArgs = "";
						- m_szReturnVal = "";
						- m_freeText = "waitingForRequest";
						- m_pCommunicationConnection = { IHandle 
							- _m2Class = "";
						}
						- m_pReceiver = { IHandle 
							- _m2Class = "IClassifierRole";
							- _id = GUID 0a699d65-0a7c-49c9-8ec4-d44fcef233e4;
						}
						- m_pSender = { IHandle 
							- _m2Class = "IClassifierRole";
							- _id = GUID 0a699d65-0a7c-49c9-8ec4-d44fcef233e4;
						}
						- m_pFormalMessage = { IHandle 
							- _m2Class = "";
						}
						- m_eType = CONDITION;
						- m_targetExec = { IHandle 
							- _m2Class = "";
						}
						- m_srcExec = { IHandle 
							- _m2Class = "";
						}
					}
					{ IMessage 
						- _id = GUID c9726350-c3ca-4f85-b5eb-44fdc32b4b9b;
						- _properties = { IPropertyContainer 
							- Subjects = { IRPYRawContainer 
								- size = 1;
								- value = 
								{ IPropertySubject 
									- _Name = "SequenceDiagram";
									- Metaclasses = { IRPYRawContainer 
										- size = 1;
										- value = 
										{ IPropertyMetaclass 
											- _Name = "Condition_Mark";
											- Properties = { IRPYRawContainer 
												- size = 1;
												- value = 
												{ IProperty 
													- _Name = "IsStateCondition";
													- _Value = "True";
													- _Type = Bool;
												}
											}
										}
									}
								}
							}
						}
						- _name = "connector";
						- _modifiedTimeWeak = 1.2.1990::0:0:0;
						- m_szSequence = "";
						- m_szActualArgs = "";
						- m_szReturnVal = "";
						- m_freeText = "Moving";
						- m_pCommunicationConnection = { IHandle 
							- _m2Class = "";
						}
						- m_pReceiver = { IHandle 
							- _m2Class = "IClassifierRole";
							- _id = GUID 0a699d65-0a7c-49c9-8ec4-d44fcef233e4;
						}
						- m_pSender = { IHandle 
							- _m2Class = "IClassifierRole";
							- _id = GUID 0a699d65-0a7c-49c9-8ec4-d44fcef233e4;
						}
						- m_pFormalMessage = { IHandle 
							- _m2Class = "";
						}
						- m_eType = CONDITION;
						- m_targetExec = { IHandle 
							- _m2Class = "";
						}
						- m_srcExec = { IHandle 
							- _m2Class = "";
						}
					}
					{ IMessage 
						- _id = GUID 7f3a1db8-6eec-4dee-ad77-5df73c8293d6;
						- _properties = { IPropertyContainer 
							- Subjects = { IRPYRawContainer 
								- size = 1;
								- value = 
								{ IPropertySubject 
									- _Name = "SequenceDiagram";
									- Metaclasses = { IRPYRawContainer 
										- size = 1;
										- value = 
										{ IPropertyMetaclass 
											- _Name = "Condition_Mark";
											- Properties = { IRPYRawContainer 
												- size = 1;
												- value = 
												{ IProperty 
													- _Name = "IsStateCondition";
													- _Value = "True";
													- _Type = Bool;
												}
											}
										}
									}
								}
							}
						}
						- _name = "connector";
						- _modifiedTimeWeak = 1.2.1990::0:0:0;
						- m_szSequence = "";
						- m_szActualArgs = "";
						- m_szReturnVal = "";
						- m_freeText = "Stopped";
						- m_pCommunicationConnection = { IHandle 
							- _m2Class = "";
						}
						- m_pReceiver = { IHandle 
							- _m2Class = "IClassifierRole";
							- _id = GUID 0a699d65-0a7c-49c9-8ec4-d44fcef233e4;
						}
						- m_pSender = { IHandle 
							- _m2Class = "IClassifierRole";
							- _id = GUID 0a699d65-0a7c-49c9-8ec4-d44fcef233e4;
						}
						- m_pFormalMessage = { IHandle 
							- _m2Class = "";
						}
						- m_eType = CONDITION;
						- m_targetExec = { IHandle 
							- _m2Class = "";
						}
						- m_srcExec = { IHandle 
							- _m2Class = "";
						}
					}
					{ IMessage 
						- _id = GUID c2e5b8d8-2bd4-4184-a8c2-9be6d315d1a9;
						- _myState = 8192;
						- _name = "DoorsOpenedController";
						- _modifiedTimeWeak = 1.2.1990::0:0:0;
						- m_szSequence = "3.";
						- m_szActualArgs = "areOpened = true";
						- m_szReturnVal = "";
						- m_pCommunicationConnection = { IHandle 
							- _m2Class = "";
						}
						- m_pReceiver = { IHandle 
							- _m2Class = "IClassifierRole";
							- _id = GUID 0a699d65-0a7c-49c9-8ec4-d44fcef233e4;
						}
						- m_pSender = { IHandle 
							- _m2Class = "IClassifierRole";
							- _id = GUID a8dfc413-d4b2-437c-99b6-e9773e0586a3;
						}
						- m_pFormalMessage = { IHandle 
							- _m2Class = "IEvent";
							- _filename = "Default.sbs";
							- _subsystem = "Default";
							- _class = "";
							- _name = "DoorsOpenedController(boolean)";
							- _id = GUID 8d9584ef-b0bf-4119-af91-fb0310eb32e2;
						}
						- m_eType = EVENT;
						- m_targetExec = { IHandle 
							- _m2Class = "";
						}
						- m_srcExec = { IHandle 
							- _m2Class = "";
						}
					}
				}
			}
		}
		{ IMSC 
			- _id = GUID 60223de8-397e-4e69-98f3-528b622631ea;
			- _myState = 8192;
			- _properties = { IPropertyContainer 
				- Subjects = { IRPYRawContainer 
					- size = 1;
					- value = 
					{ IPropertySubject 
						- _Name = "Format";
						- Metaclasses = { IRPYRawContainer 
							- size = 1;
							- value = 
							{ IPropertyMetaclass 
								- _Name = "InstanceLine";
								- Properties = { IRPYRawContainer 
									- size = 8;
									- value = 
									{ IProperty 
										- _Name = "DefaultSize";
										- _Value = "0,0,96,437";
										- _Type = String;
									}
									{ IProperty 
										- _Name = "Fill.FillColor";
										- _Value = "255,255,255";
										- _Type = Color;
									}
									{ IProperty 
										- _Name = "Font.Font";
										- _Value = "Arial";
										- _Type = String;
									}
									{ IProperty 
										- _Name = "Font.FontColor";
										- _Value = "0,0,0";
										- _Type = Color;
									}
									{ IProperty 
										- _Name = "Font.Size";
										- _Value = "10";
										- _Type = Int;
									}
									{ IProperty 
										- _Name = "Font.Weight@Child.NameCompartment@Name";
										- _Value = "$<cancel>";
										- _Type = Int;
									}
									{ IProperty 
										- _Name = "Line.LineColor";
										- _Value = "121,122,0";
										- _Type = Color;
									}
									{ IProperty 
										- _Name = "Line.LineWidth";
										- _Value = "0";
										- _Type = Int;
									}
								}
							}
						}
					}
				}
			}
			- _name = "pattern";
			- _modifiedTimeWeak = 1.1.1970::1:0:0;
			- _lastModifiedTime = "11.29.2013::8:17:16";
			- _graphicChart = { CGIMscChart 
				- vLadderMargin = 20;
				- m_usingActivationBar = 0;
				- _id = GUID aa0bf5d1-2357-4406-86a9-e6114a81b426;
				- m_type = 0;
				- m_pModelObject = { IHandle 
					- _m2Class = "IMSC";
					- _id = GUID 60223de8-397e-4e69-98f3-528b622631ea;
				}
				- m_pParent = ;
				- m_name = { CGIText 
					- m_str = "";
					- m_style = "Arial" 10 0 0 0 1 ;
					- m_color = { IColor 
						- m_fgColor = 0;
						- m_bgColor = 0;
						- m_bgFlag = 0;
					}
					- m_position = 1 0 0  ;
					- m_nIdent = 0;
					- m_bImplicitSetRectPoints = 0;
					- m_nOrientationCtrlPt = 8;
				}
				- m_drawBehavior = 0;
				- m_bIsPreferencesInitialized = 0;
				- elementList = 12;
				{ CGIBox 
					- _id = GUID 8a436a5f-22ec-41c1-80a6-b8b3cd34d2b8;
					- m_type = 108;
					- m_pModelObject = { IHandle 
						- _m2Class = "ICollaboration";
						- _id = GUID 9ed3461d-908f-4fc6-bb10-95f49926598f;
					}
					- m_pParent = ;
					- m_name = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_drawBehavior = 0;
					- m_bIsPreferencesInitialized = 0;
					- m_polygon = 0 ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
					- Compartments = { IRPYRawContainer 
						- size = 0;
					}
				}
				{ CGIMscColumnCR 
					- _id = GUID c2096ba6-9e54-4874-9463-734ad9f4e1fe;
					- m_type = 109;
					- m_pModelObject = { IHandle 
						- _m2Class = "IClassifierRole";
						- _id = GUID a9b06e81-e262-4696-ad50-8aee30fba2b1;
					}
					- m_pParent = GUID 8a436a5f-22ec-41c1-80a6-b8b3cd34d2b8;
					- m_name = { CGIText 
						- m_str = "Elevator[0]->fl[3]:Floor";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_drawBehavior = 0;
					- m_transform = 1 0 0 0.00876015 1293 50 ;
					- m_bIsPreferencesInitialized = 1;
					- m_AdditionalLabel = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 1;
					}
					- m_position = 4 0 0  0 49885  96 49885  96 0  ;
					- m_pInheritsFrom = { IHandle 
						- _m2Class = "";
					}
					- m_nInheritanceMask = 0;
					- m_SubType = 0;
				}
				{ CGIMscColumnCR 
					- _id = GUID fc9adb3a-2775-4f17-95e4-60bbf4b37f72;
					- m_type = 109;
					- m_pModelObject = { IHandle 
						- _m2Class = "IClassifierRole";
						- _id = GUID ef19249e-9725-40f7-8c7d-e5913cfbc403;
					}
					- m_pParent = GUID 8a436a5f-22ec-41c1-80a6-b8b3cd34d2b8;
					- m_name = { CGIText 
						- m_str = "Elevator[0]->fl[2]:Floor";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_drawBehavior = 0;
					- m_transform = 1 0 0 0.00876015 1187 50 ;
					- m_bIsPreferencesInitialized = 1;
					- m_AdditionalLabel = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 1;
					}
					- m_position = 4 0 0  0 49885  96 49885  96 0  ;
					- m_pInheritsFrom = { IHandle 
						- _m2Class = "";
					}
					- m_nInheritanceMask = 0;
					- m_SubType = 0;
				}
				{ CGIMscColumnCR 
					- _id = GUID c62bbf59-f7c7-4317-bc14-89d338823f45;
					- m_type = 109;
					- m_pModelObject = { IHandle 
						- _m2Class = "IClassifierRole";
						- _id = GUID e643385f-4e9d-4fbc-9338-6d12dcbb3c1a;
					}
					- m_pParent = GUID 8a436a5f-22ec-41c1-80a6-b8b3cd34d2b8;
					- m_name = { CGIText 
						- m_str = "Elevator[0]->fl[1]:Floor";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_drawBehavior = 0;
					- m_transform = 1 0 0 0.00876015 1081 50 ;
					- m_bIsPreferencesInitialized = 1;
					- m_AdditionalLabel = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 1;
					}
					- m_position = 4 0 0  0 49885  96 49885  96 0  ;
					- m_pInheritsFrom = { IHandle 
						- _m2Class = "";
					}
					- m_nInheritanceMask = 0;
					- m_SubType = 0;
				}
				{ CGIMscColumnCR 
					- _id = GUID 2cee1145-c36b-4a80-b581-6fdec6160dda;
					- m_type = 109;
					- m_pModelObject = { IHandle 
						- _m2Class = "IClassifierRole";
						- _id = GUID e3cdf9f9-89fe-4a9f-b3cc-130d1681a55d;
					}
					- m_pParent = GUID 8a436a5f-22ec-41c1-80a6-b8b3cd34d2b8;
					- m_name = { CGIText 
						- m_str = "Elevator[0]->fl[0]:Floor";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_drawBehavior = 0;
					- m_transform = 1 0 0 0.00876015 975 50 ;
					- m_bIsPreferencesInitialized = 1;
					- m_AdditionalLabel = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 1;
					}
					- m_position = 4 0 0  0 49885  96 49885  96 0  ;
					- m_pInheritsFrom = { IHandle 
						- _m2Class = "";
					}
					- m_nInheritanceMask = 0;
					- m_SubType = 0;
				}
				{ CGIMscColumnCR 
					- _id = GUID d9810e4d-ea05-426b-8ab6-4c13c582fc2d;
					- m_type = 109;
					- m_pModelObject = { IHandle 
						- _m2Class = "IClassifierRole";
						- _id = GUID 2cb2c377-9022-4eb5-b8bf-6cc94b5f1f2a;
					}
					- m_pParent = GUID 8a436a5f-22ec-41c1-80a6-b8b3cd34d2b8;
					- m_name = { CGIText 
						- m_str = "Elevator[0]->hc->en:Engine";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_drawBehavior = 0;
					- m_transform = 1 0 0 0.00876015 820 50 ;
					- m_bIsPreferencesInitialized = 1;
					- m_AdditionalLabel = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 1;
					}
					- m_position = 4 0 0  0 49885  96 49885  96 0  ;
					- m_pInheritsFrom = { IHandle 
						- _m2Class = "";
					}
					- m_nInheritanceMask = 0;
					- m_SubType = 0;
				}
				{ CGIMscColumnCR 
					- _id = GUID 7627e2df-c76c-4412-a380-a6a08fd2a903;
					- m_type = 109;
					- m_pModelObject = { IHandle 
						- _m2Class = "IClassifierRole";
						- _id = GUID a827731a-919f-4824-87cf-3da5d78f2a4a;
					}
					- m_pParent = GUID 8a436a5f-22ec-41c1-80a6-b8b3cd34d2b8;
					- m_name = { CGIText 
						- m_str = "Elevator[0]->mc:MoveController";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_drawBehavior = 0;
					- m_transform = 1 0 0 0.00876015 680 50 ;
					- m_bIsPreferencesInitialized = 1;
					- m_AdditionalLabel = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 1;
					}
					- m_position = 4 0 0  0 49885  96 49885  96 0  ;
					- m_pInheritsFrom = { IHandle 
						- _m2Class = "";
					}
					- m_nInheritanceMask = 0;
					- m_SubType = 0;
				}
				{ CGIMscColumnCR 
					- _id = GUID 479ea3e3-ab9e-43d0-94b4-1417206ac567;
					- m_type = 109;
					- m_pModelObject = { IHandle 
						- _m2Class = "IClassifierRole";
						- _id = GUID 5fcf4aff-81a7-4aa1-be4d-32819e35f9cd;
					}
					- m_pParent = GUID 8a436a5f-22ec-41c1-80a6-b8b3cd34d2b8;
					- m_name = { CGIText 
						- m_str = "Elevator[0]->rc:ReadyController";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_drawBehavior = 0;
					- m_transform = 1 0 0 0.00876015 564 50 ;
					- m_bIsPreferencesInitialized = 1;
					- m_AdditionalLabel = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 1;
					}
					- m_position = 4 0 0  0 49885  96 49885  96 0  ;
					- m_pInheritsFrom = { IHandle 
						- _m2Class = "";
					}
					- m_nInheritanceMask = 0;
					- m_SubType = 0;
				}
				{ CGIMscColumnCR 
					- _id = GUID dfb8f1c8-580e-4056-8eaf-628a5eb9d3a6;
					- m_type = 109;
					- m_pModelObject = { IHandle 
						- _m2Class = "IClassifierRole";
						- _id = GUID 99803058-1125-4c36-bde3-4ffe59699fb2;
					}
					- m_pParent = GUID 8a436a5f-22ec-41c1-80a6-b8b3cd34d2b8;
					- m_name = { CGIText 
						- m_str = "Elevator[0]->lc:LoadController";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_drawBehavior = 0;
					- m_transform = 1 0 0 0.00876015 458 50 ;
					- m_bIsPreferencesInitialized = 1;
					- m_AdditionalLabel = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 1;
					}
					- m_position = 4 0 0  0 49885  96 49885  96 0  ;
					- m_pInheritsFrom = { IHandle 
						- _m2Class = "";
					}
					- m_nInheritanceMask = 0;
					- m_SubType = 0;
				}
				{ CGIMscColumnCR 
					- _id = GUID 841f18f7-f403-4b3d-8a00-f2a06e1612db;
					- m_type = 109;
					- m_pModelObject = { IHandle 
						- _m2Class = "IClassifierRole";
						- _id = GUID 0ed70c94-72c7-48a1-854a-60ceb43e3dac;
					}
					- m_pParent = GUID 8a436a5f-22ec-41c1-80a6-b8b3cd34d2b8;
					- m_name = { CGIText 
						- m_str = "Elevator[0]->hc:HeightController";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_drawBehavior = 0;
					- m_transform = 1 0 0 0.00876015 343 50 ;
					- m_bIsPreferencesInitialized = 1;
					- m_AdditionalLabel = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 1;
					}
					- m_position = 4 0 0  0 49885  96 49885  96 0  ;
					- m_pInheritsFrom = { IHandle 
						- _m2Class = "";
					}
					- m_nInheritanceMask = 0;
					- m_SubType = 0;
				}
				{ CGIMscColumnCR 
					- _id = GUID 4475e224-79d2-4183-81c4-e1303c42f1d8;
					- m_type = 109;
					- m_pModelObject = { IHandle 
						- _m2Class = "IClassifierRole";
						- _id = GUID efe17c13-faec-4cce-9913-649e1b6bf7cb;
					}
					- m_pParent = GUID 8a436a5f-22ec-41c1-80a6-b8b3cd34d2b8;
					- m_name = { CGIText 
						- m_str = "Elevator[0]->dc:DoorsController";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_drawBehavior = 0;
					- m_transform = 1 0 0 0.00876015 237 50 ;
					- m_bIsPreferencesInitialized = 1;
					- m_AdditionalLabel = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 1;
					}
					- m_position = 4 0 0  0 49885  96 49885  96 0  ;
					- m_pInheritsFrom = { IHandle 
						- _m2Class = "";
					}
					- m_nInheritanceMask = 0;
					- m_SubType = 0;
				}
				{ CGIMscColumnCR 
					- _id = GUID ae4f7a10-50a7-4347-8949-9287b024bafb;
					- m_type = 109;
					- m_pModelObject = { IHandle 
						- _m2Class = "IClassifierRole";
						- _id = GUID 40d9c16a-d72f-4024-820d-f1874a4ff1ab;
					}
					- m_pParent = GUID 8a436a5f-22ec-41c1-80a6-b8b3cd34d2b8;
					- m_name = { CGIText 
						- m_str = "Elevator[0]:Elevator";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_drawBehavior = 0;
					- m_transform = 1 0 0 0.00876015 118 50 ;
					- m_bIsPreferencesInitialized = 1;
					- m_AdditionalLabel = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 1;
					}
					- m_position = 4 0 0  0 49885  96 49885  96 0  ;
					- m_pInheritsFrom = { IHandle 
						- _m2Class = "";
					}
					- m_nInheritanceMask = 0;
					- m_SubType = 0;
				}
				
				- m_access = 'Z';
				- m_modified = 'N';
				- m_fileVersion = "";
				- m_nModifyDate = 0;
				- m_nCreateDate = 0;
				- m_creator = "";
				- m_bScaleWithZoom = 1;
				- m_arrowStyle = 'S';
				- m_pRoot = GUID 8a436a5f-22ec-41c1-80a6-b8b3cd34d2b8;
				- m_currentLeftTop = 0 0 ;
				- m_currentRightBottom = 0 0 ;
			}
			- _defaultSubsystem = { IHandle 
				- _m2Class = "ISubsystem";
				- _filename = "Default.sbs";
				- _subsystem = "";
				- _class = "";
				- _name = "Default";
				- _id = GUID 2970263e-bdf6-4006-ba3e-12cef9acae52;
			}
			- m_pICollaboration = { ICollaboration 
				- _id = GUID 9ed3461d-908f-4fc6-bb10-95f49926598f;
				- _modifiedTimeWeak = 1.1.1970::1:0:0;
				- ClassifierRoles = { IRPYRawContainer 
					- size = 11;
					- value = 
					{ IClassifierRole 
						- _id = GUID efe17c13-faec-4cce-9913-649e1b6bf7cb;
						- _name = "Elevator[0]->dc";
						- _modifiedTimeWeak = 1.1.1970::1:0:0;
						- m_eRoleType = CLASS;
						- m_pBase = { IHandle 
							- _m2Class = "IClass";
							- _filename = "Default.sbs";
							- _subsystem = "Default";
							- _class = "";
							- _name = "DoorsController";
							- _id = GUID 38aec46c-a896-46bc-bad4-16c77e5569d0;
						}
						- m_instance = { IHandle 
							- _m2Class = "";
						}
					}
					{ IClassifierRole 
						- _id = GUID 40d9c16a-d72f-4024-820d-f1874a4ff1ab;
						- _name = "Elevator[0]";
						- _modifiedTimeWeak = 1.1.1970::1:0:0;
						- m_eRoleType = CLASS;
						- m_pBase = { IHandle 
							- _m2Class = "IClass";
							- _filename = "Default.sbs";
							- _subsystem = "Default";
							- _class = "";
							- _name = "Elevator";
							- _id = GUID 6e9ca01c-040b-4e85-bbc9-4f7798db5ef4;
						}
						- m_instance = { IHandle 
							- _m2Class = "";
						}
					}
					{ IClassifierRole 
						- _id = GUID e3cdf9f9-89fe-4a9f-b3cc-130d1681a55d;
						- _name = "Elevator[0]->fl[0]";
						- _modifiedTimeWeak = 1.1.1970::1:0:0;
						- m_eRoleType = CLASS;
						- m_pBase = { IHandle 
							- _m2Class = "IClass";
							- _filename = "Default.sbs";
							- _subsystem = "Default";
							- _class = "";
							- _name = "Floor";
							- _id = GUID 7270c741-82dd-4d79-a637-77a3d1fb86d5;
						}
						- m_instance = { IHandle 
							- _m2Class = "";
						}
					}
					{ IClassifierRole 
						- _id = GUID e643385f-4e9d-4fbc-9338-6d12dcbb3c1a;
						- _name = "Elevator[0]->fl[1]";
						- _modifiedTimeWeak = 1.1.1970::1:0:0;
						- m_eRoleType = CLASS;
						- m_pBase = { IHandle 
							- _m2Class = "IClass";
							- _filename = "Default.sbs";
							- _subsystem = "Default";
							- _class = "";
							- _name = "Floor";
							- _id = GUID 7270c741-82dd-4d79-a637-77a3d1fb86d5;
						}
						- m_instance = { IHandle 
							- _m2Class = "";
						}
					}
					{ IClassifierRole 
						- _id = GUID ef19249e-9725-40f7-8c7d-e5913cfbc403;
						- _name = "Elevator[0]->fl[2]";
						- _modifiedTimeWeak = 1.1.1970::1:0:0;
						- m_eRoleType = CLASS;
						- m_pBase = { IHandle 
							- _m2Class = "IClass";
							- _filename = "Default.sbs";
							- _subsystem = "Default";
							- _class = "";
							- _name = "Floor";
							- _id = GUID 7270c741-82dd-4d79-a637-77a3d1fb86d5;
						}
						- m_instance = { IHandle 
							- _m2Class = "";
						}
					}
					{ IClassifierRole 
						- _id = GUID a9b06e81-e262-4696-ad50-8aee30fba2b1;
						- _name = "Elevator[0]->fl[3]";
						- _modifiedTimeWeak = 1.1.1970::1:0:0;
						- m_eRoleType = CLASS;
						- m_pBase = { IHandle 
							- _m2Class = "IClass";
							- _filename = "Default.sbs";
							- _subsystem = "Default";
							- _class = "";
							- _name = "Floor";
							- _id = GUID 7270c741-82dd-4d79-a637-77a3d1fb86d5;
						}
						- m_instance = { IHandle 
							- _m2Class = "";
						}
					}
					{ IClassifierRole 
						- _id = GUID 0ed70c94-72c7-48a1-854a-60ceb43e3dac;
						- _name = "Elevator[0]->hc";
						- _modifiedTimeWeak = 1.1.1970::1:0:0;
						- m_eRoleType = CLASS;
						- m_pBase = { IHandle 
							- _m2Class = "IClass";
							- _filename = "Default.sbs";
							- _subsystem = "Default";
							- _class = "";
							- _name = "HeightController";
							- _id = GUID 33dfe780-1e75-49ee-9e55-834dc5fafe51;
						}
						- m_instance = { IHandle 
							- _m2Class = "";
						}
					}
					{ IClassifierRole 
						- _id = GUID 99803058-1125-4c36-bde3-4ffe59699fb2;
						- _name = "Elevator[0]->lc";
						- _modifiedTimeWeak = 1.1.1970::1:0:0;
						- m_eRoleType = CLASS;
						- m_pBase = { IHandle 
							- _m2Class = "IClass";
							- _filename = "Default.sbs";
							- _subsystem = "Default";
							- _class = "";
							- _name = "LoadController";
							- _id = GUID d1dd4690-acd6-41ad-8f2a-b8600ecd3f36;
						}
						- m_instance = { IHandle 
							- _m2Class = "";
						}
					}
					{ IClassifierRole 
						- _id = GUID a827731a-919f-4824-87cf-3da5d78f2a4a;
						- _name = "Elevator[0]->mc";
						- _modifiedTimeWeak = 1.1.1970::1:0:0;
						- m_eRoleType = CLASS;
						- m_pBase = { IHandle 
							- _m2Class = "IClass";
							- _filename = "Default.sbs";
							- _subsystem = "Default";
							- _class = "";
							- _name = "MoveController";
							- _id = GUID d88479c4-1e3a-4ccb-8784-cfe96908d02b;
						}
						- m_instance = { IHandle 
							- _m2Class = "";
						}
					}
					{ IClassifierRole 
						- _id = GUID 5fcf4aff-81a7-4aa1-be4d-32819e35f9cd;
						- _name = "Elevator[0]->rc";
						- _modifiedTimeWeak = 1.1.1970::1:0:0;
						- m_eRoleType = CLASS;
						- m_pBase = { IHandle 
							- _m2Class = "IClass";
							- _filename = "Default.sbs";
							- _subsystem = "Default";
							- _class = "";
							- _name = "ReadyController";
							- _id = GUID 953be687-ea04-4796-b2b4-1ac0aa636051;
						}
						- m_instance = { IHandle 
							- _m2Class = "";
						}
					}
					{ IClassifierRole 
						- _id = GUID 2cb2c377-9022-4eb5-b8bf-6cc94b5f1f2a;
						- _name = "Elevator[0]->hc->en";
						- _modifiedTimeWeak = 1.1.1970::1:0:0;
						- m_eRoleType = CLASS;
						- m_pBase = { IHandle 
							- _m2Class = "IClass";
							- _filename = "Default.sbs";
							- _subsystem = "Default";
							- _class = "";
							- _name = "Engine";
							- _id = GUID 0fbd8080-b925-4cf0-8f63-7d60c45a83ce;
						}
						- m_instance = { IHandle 
							- _m2Class = "";
						}
					}
				}
			}
		}
		{ IMSC 
			- _id = GUID 25d1c925-319d-4641-997b-2c26503553b4;
			- _myState = 8192;
			- _properties = { IPropertyContainer 
				- Subjects = { IRPYRawContainer 
					- size = 1;
					- value = 
					{ IPropertySubject 
						- _Name = "Format";
						- Metaclasses = { IRPYRawContainer 
							- size = 4;
							- value = 
							{ IPropertyMetaclass 
								- _Name = "Condition_Mark";
								- Properties = { IRPYRawContainer 
									- size = 8;
									- value = 
									{ IProperty 
										- _Name = "DefaultSize";
										- _Value = "0,0,67,39";
										- _Type = String;
									}
									{ IProperty 
										- _Name = "Fill.FillColor";
										- _Value = "255,255,255";
										- _Type = Color;
									}
									{ IProperty 
										- _Name = "Font.Font";
										- _Value = "Arial";
										- _Type = String;
									}
									{ IProperty 
										- _Name = "Font.FontColor";
										- _Value = "0,0,0";
										- _Type = Color;
									}
									{ IProperty 
										- _Name = "Font.Size";
										- _Value = "10";
										- _Type = Int;
									}
									{ IProperty 
										- _Name = "Font.Weight@Child.NameCompartment@Name";
										- _Value = "$<cancel>";
										- _Type = Int;
									}
									{ IProperty 
										- _Name = "Line.LineColor";
										- _Value = "0,112,0";
										- _Type = Color;
									}
									{ IProperty 
										- _Name = "Line.LineWidth";
										- _Value = "1";
										- _Type = Int;
									}
								}
							}
							{ IPropertyMetaclass 
								- _Name = "InstanceLine";
								- Properties = { IRPYRawContainer 
									- size = 8;
									- value = 
									{ IProperty 
										- _Name = "DefaultSize";
										- _Value = "0,0,96,437";
										- _Type = String;
									}
									{ IProperty 
										- _Name = "Fill.FillColor";
										- _Value = "255,255,255";
										- _Type = Color;
									}
									{ IProperty 
										- _Name = "Font.Font";
										- _Value = "Arial";
										- _Type = String;
									}
									{ IProperty 
										- _Name = "Font.FontColor";
										- _Value = "0,0,0";
										- _Type = Color;
									}
									{ IProperty 
										- _Name = "Font.Size";
										- _Value = "10";
										- _Type = Int;
									}
									{ IProperty 
										- _Name = "Font.Weight@Child.NameCompartment@Name";
										- _Value = "$<cancel>";
										- _Type = Int;
									}
									{ IProperty 
										- _Name = "Line.LineColor";
										- _Value = "121,122,0";
										- _Type = Color;
									}
									{ IProperty 
										- _Name = "Line.LineWidth";
										- _Value = "0";
										- _Type = Int;
									}
								}
							}
							{ IPropertyMetaclass 
								- _Name = "Message";
								- Properties = { IRPYRawContainer 
									- size = 5;
									- value = 
									{ IProperty 
										- _Name = "Font.Font";
										- _Value = "Arial";
										- _Type = String;
									}
									{ IProperty 
										- _Name = "Font.FontColor";
										- _Value = "0,0,128";
										- _Type = Color;
									}
									{ IProperty 
										- _Name = "Font.Size";
										- _Value = "10";
										- _Type = Int;
									}
									{ IProperty 
										- _Name = "Line.LineColor";
										- _Value = "0,112,0";
										- _Type = Color;
									}
									{ IProperty 
										- _Name = "Line.LineWidth";
										- _Value = "1";
										- _Type = Int;
									}
								}
							}
							{ IPropertyMetaclass 
								- _Name = "TimeoutMessage";
								- Properties = { IRPYRawContainer 
									- size = 5;
									- value = 
									{ IProperty 
										- _Name = "Font.Font";
										- _Value = "Arial";
										- _Type = String;
									}
									{ IProperty 
										- _Name = "Font.FontColor";
										- _Value = "0,0,128";
										- _Type = Color;
									}
									{ IProperty 
										- _Name = "Font.Size";
										- _Value = "10";
										- _Type = Int;
									}
									{ IProperty 
										- _Name = "Line.LineColor";
										- _Value = "0,112,0";
										- _Type = Color;
									}
									{ IProperty 
										- _Name = "Line.LineWidth";
										- _Value = "1";
										- _Type = Int;
									}
								}
							}
						}
					}
				}
			}
			- _name = "Animated pattern";
			- _modifiedTimeWeak = 1.1.1970::1:0:0;
			- _lastModifiedTime = "11.29.2013::8:28:50";
			- _graphicChart = { CGIMscChart 
				- vLadderMargin = 20;
				- m_usingActivationBar = 0;
				- _id = GUID fb6f82ae-2d93-45ed-b9a6-54da21c613ae;
				- m_type = 0;
				- m_pModelObject = { IHandle 
					- _m2Class = "IMSC";
					- _id = GUID 25d1c925-319d-4641-997b-2c26503553b4;
				}
				- m_pParent = ;
				- m_name = { CGIText 
					- m_str = "";
					- m_style = "Arial" 10 0 0 0 1 ;
					- m_color = { IColor 
						- m_fgColor = 0;
						- m_bgColor = 0;
						- m_bgFlag = 0;
					}
					- m_position = 1 0 0  ;
					- m_nIdent = 0;
					- m_bImplicitSetRectPoints = 0;
					- m_nOrientationCtrlPt = 8;
				}
				- m_drawBehavior = 0;
				- m_bIsPreferencesInitialized = 0;
				- elementList = 52;
				{ CGIBox 
					- _id = GUID da6e79a0-5f33-4349-b105-cee25cf8f8f0;
					- m_type = 108;
					- m_pModelObject = { IHandle 
						- _m2Class = "ICollaboration";
						- _id = GUID 4adbd3f9-f1ef-4bcd-834c-36d32cc8e86d;
					}
					- m_pParent = ;
					- m_name = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_drawBehavior = 0;
					- m_bIsPreferencesInitialized = 0;
					- m_polygon = 0 ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
					- Compartments = { IRPYRawContainer 
						- size = 0;
					}
				}
				{ CGIMscColumnCR 
					- _id = GUID c6e227c0-ac5c-4c36-90c6-47536000dd70;
					- _properties = { IPropertyContainer 
						- Subjects = { IRPYRawContainer 
							- size = 1;
							- value = 
							{ IPropertySubject 
								- _Name = "Format";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "InstanceLine";
										- Properties = { IRPYRawContainer 
											- size = 8;
											- value = 
											{ IProperty 
												- _Name = "DefaultSize";
												- _Value = "0,0,96,437";
												- _Type = String;
											}
											{ IProperty 
												- _Name = "Fill.FillColor";
												- _Value = "255,255,255";
												- _Type = Color;
											}
											{ IProperty 
												- _Name = "Font.Font";
												- _Value = "Arial";
												- _Type = String;
											}
											{ IProperty 
												- _Name = "Font.FontColor";
												- _Value = "0,0,0";
												- _Type = Color;
											}
											{ IProperty 
												- _Name = "Font.Size";
												- _Value = "10";
												- _Type = Int;
											}
											{ IProperty 
												- _Name = "Font.Weight@Child.NameCompartment@Name";
												- _Value = "$<cancel>";
												- _Type = Int;
											}
											{ IProperty 
												- _Name = "Line.LineColor";
												- _Value = "121,122,0";
												- _Type = Color;
											}
											{ IProperty 
												- _Name = "Line.LineWidth";
												- _Value = "0";
												- _Type = Int;
											}
										}
									}
								}
							}
						}
					}
					- m_type = 109;
					- m_pModelObject = { IHandle 
						- _m2Class = "IClassifierRole";
						- _id = GUID d512c32f-f665-410c-bc5c-c268d0c64648;
					}
					- m_pParent = GUID da6e79a0-5f33-4349-b105-cee25cf8f8f0;
					- m_name = { CGIText 
						- m_str = "Elevator[0]->dc:DoorsController";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_drawBehavior = 0;
					- m_transform = 1 0 0 0.0536835 1087 50 ;
					- m_bIsPreferencesInitialized = 0;
					- m_AdditionalLabel = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 1;
					}
					- m_position = 1 0 0  ;
					- m_pInheritsFrom = { IHandle 
						- _m2Class = "";
					}
					- m_nInheritanceMask = 0;
					- m_SubType = 0;
				}
				{ CGIMscColumnCR 
					- _id = GUID 8ee83f03-e542-49ea-9ca7-be0a407d6529;
					- _properties = { IPropertyContainer 
						- Subjects = { IRPYRawContainer 
							- size = 1;
							- value = 
							{ IPropertySubject 
								- _Name = "Format";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "InstanceLine";
										- Properties = { IRPYRawContainer 
											- size = 8;
											- value = 
											{ IProperty 
												- _Name = "DefaultSize";
												- _Value = "0,0,96,437";
												- _Type = String;
											}
											{ IProperty 
												- _Name = "Fill.FillColor";
												- _Value = "255,255,255";
												- _Type = Color;
											}
											{ IProperty 
												- _Name = "Font.Font";
												- _Value = "Arial";
												- _Type = String;
											}
											{ IProperty 
												- _Name = "Font.FontColor";
												- _Value = "0,0,0";
												- _Type = Color;
											}
											{ IProperty 
												- _Name = "Font.Size";
												- _Value = "10";
												- _Type = Int;
											}
											{ IProperty 
												- _Name = "Font.Weight@Child.NameCompartment@Name";
												- _Value = "$<cancel>";
												- _Type = Int;
											}
											{ IProperty 
												- _Name = "Line.LineColor";
												- _Value = "121,122,0";
												- _Type = Color;
											}
											{ IProperty 
												- _Name = "Line.LineWidth";
												- _Value = "0";
												- _Type = Int;
											}
										}
									}
								}
							}
						}
					}
					- m_type = 109;
					- m_pModelObject = { IHandle 
						- _m2Class = "IClassifierRole";
						- _id = GUID d3a77353-9933-4ff7-b408-56cd6622e5ea;
					}
					- m_pParent = GUID da6e79a0-5f33-4349-b105-cee25cf8f8f0;
					- m_name = { CGIText 
						- m_str = "Elevator[0]:Elevator";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_drawBehavior = 0;
					- m_transform = 1 0 0 0.0536835 118 50 ;
					- m_bIsPreferencesInitialized = 0;
					- m_AdditionalLabel = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 1;
					}
					- m_position = 1 0 0  ;
					- m_pInheritsFrom = { IHandle 
						- _m2Class = "";
					}
					- m_nInheritanceMask = 0;
					- m_SubType = 0;
				}
				{ CGIMscColumnCR 
					- _id = GUID c7de0033-fba0-474d-b8a6-7f495928f52c;
					- _properties = { IPropertyContainer 
						- Subjects = { IRPYRawContainer 
							- size = 1;
							- value = 
							{ IPropertySubject 
								- _Name = "Format";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "InstanceLine";
										- Properties = { IRPYRawContainer 
											- size = 8;
											- value = 
											{ IProperty 
												- _Name = "DefaultSize";
												- _Value = "0,0,96,437";
												- _Type = String;
											}
											{ IProperty 
												- _Name = "Fill.FillColor";
												- _Value = "255,255,255";
												- _Type = Color;
											}
											{ IProperty 
												- _Name = "Font.Font";
												- _Value = "Arial";
												- _Type = String;
											}
											{ IProperty 
												- _Name = "Font.FontColor";
												- _Value = "0,0,0";
												- _Type = Color;
											}
											{ IProperty 
												- _Name = "Font.Size";
												- _Value = "10";
												- _Type = Int;
											}
											{ IProperty 
												- _Name = "Font.Weight@Child.NameCompartment@Name";
												- _Value = "$<cancel>";
												- _Type = Int;
											}
											{ IProperty 
												- _Name = "Line.LineColor";
												- _Value = "121,122,0";
												- _Type = Color;
											}
											{ IProperty 
												- _Name = "Line.LineWidth";
												- _Value = "0";
												- _Type = Int;
											}
										}
									}
								}
							}
						}
					}
					- m_type = 109;
					- m_pModelObject = { IHandle 
						- _m2Class = "IClassifierRole";
						- _id = GUID d0944990-686e-4a73-93d5-65d76ec5dcd6;
					}
					- m_pParent = GUID da6e79a0-5f33-4349-b105-cee25cf8f8f0;
					- m_name = { CGIText 
						- m_str = "Elevator[0]->fl[0]:Floor";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_drawBehavior = 0;
					- m_transform = 1 0 0 0.0536835 1193 50 ;
					- m_bIsPreferencesInitialized = 0;
					- m_AdditionalLabel = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 1;
					}
					- m_position = 1 0 0  ;
					- m_pInheritsFrom = { IHandle 
						- _m2Class = "";
					}
					- m_nInheritanceMask = 0;
					- m_SubType = 0;
				}
				{ CGIMscColumnCR 
					- _id = GUID caf3d677-1da5-4a2f-9511-89cd7e1e12a0;
					- _properties = { IPropertyContainer 
						- Subjects = { IRPYRawContainer 
							- size = 1;
							- value = 
							{ IPropertySubject 
								- _Name = "Format";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "InstanceLine";
										- Properties = { IRPYRawContainer 
											- size = 8;
											- value = 
											{ IProperty 
												- _Name = "DefaultSize";
												- _Value = "0,0,96,437";
												- _Type = String;
											}
											{ IProperty 
												- _Name = "Fill.FillColor";
												- _Value = "255,255,255";
												- _Type = Color;
											}
											{ IProperty 
												- _Name = "Font.Font";
												- _Value = "Arial";
												- _Type = String;
											}
											{ IProperty 
												- _Name = "Font.FontColor";
												- _Value = "0,0,0";
												- _Type = Color;
											}
											{ IProperty 
												- _Name = "Font.Size";
												- _Value = "10";
												- _Type = Int;
											}
											{ IProperty 
												- _Name = "Font.Weight@Child.NameCompartment@Name";
												- _Value = "$<cancel>";
												- _Type = Int;
											}
											{ IProperty 
												- _Name = "Line.LineColor";
												- _Value = "121,122,0";
												- _Type = Color;
											}
											{ IProperty 
												- _Name = "Line.LineWidth";
												- _Value = "0";
												- _Type = Int;
											}
										}
									}
								}
							}
						}
					}
					- m_type = 109;
					- m_pModelObject = { IHandle 
						- _m2Class = "IClassifierRole";
						- _id = GUID 9adab9c6-343b-4de1-9c8b-935b366c3626;
					}
					- m_pParent = GUID da6e79a0-5f33-4349-b105-cee25cf8f8f0;
					- m_name = { CGIText 
						- m_str = "Elevator[0]->fl[1]:Floor";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_drawBehavior = 0;
					- m_transform = 1 0 0 0.0536835 1299 50 ;
					- m_bIsPreferencesInitialized = 0;
					- m_AdditionalLabel = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 1;
					}
					- m_position = 1 0 0  ;
					- m_pInheritsFrom = { IHandle 
						- _m2Class = "";
					}
					- m_nInheritanceMask = 0;
					- m_SubType = 0;
				}
				{ CGIMscColumnCR 
					- _id = GUID baa3765b-1174-4e81-a465-766901c84638;
					- _properties = { IPropertyContainer 
						- Subjects = { IRPYRawContainer 
							- size = 1;
							- value = 
							{ IPropertySubject 
								- _Name = "Format";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "InstanceLine";
										- Properties = { IRPYRawContainer 
											- size = 8;
											- value = 
											{ IProperty 
												- _Name = "DefaultSize";
												- _Value = "0,0,96,437";
												- _Type = String;
											}
											{ IProperty 
												- _Name = "Fill.FillColor";
												- _Value = "255,255,255";
												- _Type = Color;
											}
											{ IProperty 
												- _Name = "Font.Font";
												- _Value = "Arial";
												- _Type = String;
											}
											{ IProperty 
												- _Name = "Font.FontColor";
												- _Value = "0,0,0";
												- _Type = Color;
											}
											{ IProperty 
												- _Name = "Font.Size";
												- _Value = "10";
												- _Type = Int;
											}
											{ IProperty 
												- _Name = "Font.Weight@Child.NameCompartment@Name";
												- _Value = "$<cancel>";
												- _Type = Int;
											}
											{ IProperty 
												- _Name = "Line.LineColor";
												- _Value = "121,122,0";
												- _Type = Color;
											}
											{ IProperty 
												- _Name = "Line.LineWidth";
												- _Value = "0";
												- _Type = Int;
											}
										}
									}
								}
							}
						}
					}
					- m_type = 109;
					- m_pModelObject = { IHandle 
						- _m2Class = "IClassifierRole";
						- _id = GUID 49ff505d-fb89-490d-9cf2-db66b92be4e4;
					}
					- m_pParent = GUID da6e79a0-5f33-4349-b105-cee25cf8f8f0;
					- m_name = { CGIText 
						- m_str = "Elevator[0]->fl[2]:Floor";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_drawBehavior = 0;
					- m_transform = 1 0 0 0.0536835 1405 50 ;
					- m_bIsPreferencesInitialized = 0;
					- m_AdditionalLabel = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 1;
					}
					- m_position = 1 0 0  ;
					- m_pInheritsFrom = { IHandle 
						- _m2Class = "";
					}
					- m_nInheritanceMask = 0;
					- m_SubType = 0;
				}
				{ CGIMscColumnCR 
					- _id = GUID e349d36c-feec-4937-88c3-2326965f4c08;
					- _properties = { IPropertyContainer 
						- Subjects = { IRPYRawContainer 
							- size = 1;
							- value = 
							{ IPropertySubject 
								- _Name = "Format";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "InstanceLine";
										- Properties = { IRPYRawContainer 
											- size = 8;
											- value = 
											{ IProperty 
												- _Name = "DefaultSize";
												- _Value = "0,0,96,437";
												- _Type = String;
											}
											{ IProperty 
												- _Name = "Fill.FillColor";
												- _Value = "255,255,255";
												- _Type = Color;
											}
											{ IProperty 
												- _Name = "Font.Font";
												- _Value = "Arial";
												- _Type = String;
											}
											{ IProperty 
												- _Name = "Font.FontColor";
												- _Value = "0,0,0";
												- _Type = Color;
											}
											{ IProperty 
												- _Name = "Font.Size";
												- _Value = "10";
												- _Type = Int;
											}
											{ IProperty 
												- _Name = "Font.Weight@Child.NameCompartment@Name";
												- _Value = "$<cancel>";
												- _Type = Int;
											}
											{ IProperty 
												- _Name = "Line.LineColor";
												- _Value = "121,122,0";
												- _Type = Color;
											}
											{ IProperty 
												- _Name = "Line.LineWidth";
												- _Value = "0";
												- _Type = Int;
											}
										}
									}
								}
							}
						}
					}
					- m_type = 109;
					- m_pModelObject = { IHandle 
						- _m2Class = "IClassifierRole";
						- _id = GUID f0ff936f-4f00-4f41-a160-4d217f0d6276;
					}
					- m_pParent = GUID da6e79a0-5f33-4349-b105-cee25cf8f8f0;
					- m_name = { CGIText 
						- m_str = "Elevator[0]->fl[3]:Floor";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_drawBehavior = 0;
					- m_transform = 1 0 0 0.0536835 1511 50 ;
					- m_bIsPreferencesInitialized = 0;
					- m_AdditionalLabel = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 1;
					}
					- m_position = 1 0 0  ;
					- m_pInheritsFrom = { IHandle 
						- _m2Class = "";
					}
					- m_nInheritanceMask = 0;
					- m_SubType = 0;
				}
				{ CGIMscColumnCR 
					- _id = GUID 74159e86-6131-425a-8cba-5fc6a6fd9a97;
					- _properties = { IPropertyContainer 
						- Subjects = { IRPYRawContainer 
							- size = 1;
							- value = 
							{ IPropertySubject 
								- _Name = "Format";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "InstanceLine";
										- Properties = { IRPYRawContainer 
											- size = 8;
											- value = 
											{ IProperty 
												- _Name = "DefaultSize";
												- _Value = "0,0,96,437";
												- _Type = String;
											}
											{ IProperty 
												- _Name = "Fill.FillColor";
												- _Value = "255,255,255";
												- _Type = Color;
											}
											{ IProperty 
												- _Name = "Font.Font";
												- _Value = "Arial";
												- _Type = String;
											}
											{ IProperty 
												- _Name = "Font.FontColor";
												- _Value = "0,0,0";
												- _Type = Color;
											}
											{ IProperty 
												- _Name = "Font.Size";
												- _Value = "10";
												- _Type = Int;
											}
											{ IProperty 
												- _Name = "Font.Weight@Child.NameCompartment@Name";
												- _Value = "$<cancel>";
												- _Type = Int;
											}
											{ IProperty 
												- _Name = "Line.LineColor";
												- _Value = "121,122,0";
												- _Type = Color;
											}
											{ IProperty 
												- _Name = "Line.LineWidth";
												- _Value = "0";
												- _Type = Int;
											}
										}
									}
								}
							}
						}
					}
					- m_type = 109;
					- m_pModelObject = { IHandle 
						- _m2Class = "IClassifierRole";
						- _id = GUID b6b00713-6e03-4ec0-95ab-f01b5db15738;
					}
					- m_pParent = GUID da6e79a0-5f33-4349-b105-cee25cf8f8f0;
					- m_name = { CGIText 
						- m_str = "Elevator[0]->hc:HeightController";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_drawBehavior = 0;
					- m_transform = 1 0 0 0.0536835 249 50 ;
					- m_bIsPreferencesInitialized = 0;
					- m_AdditionalLabel = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 1;
					}
					- m_position = 1 0 0  ;
					- m_pInheritsFrom = { IHandle 
						- _m2Class = "";
					}
					- m_nInheritanceMask = 0;
					- m_SubType = 0;
				}
				{ CGIMscColumnCR 
					- _id = GUID 4394cf84-e62e-4673-8a0e-c83d75aa0c18;
					- _properties = { IPropertyContainer 
						- Subjects = { IRPYRawContainer 
							- size = 1;
							- value = 
							{ IPropertySubject 
								- _Name = "Format";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "InstanceLine";
										- Properties = { IRPYRawContainer 
											- size = 8;
											- value = 
											{ IProperty 
												- _Name = "DefaultSize";
												- _Value = "0,0,96,437";
												- _Type = String;
											}
											{ IProperty 
												- _Name = "Fill.FillColor";
												- _Value = "255,255,255";
												- _Type = Color;
											}
											{ IProperty 
												- _Name = "Font.Font";
												- _Value = "Arial";
												- _Type = String;
											}
											{ IProperty 
												- _Name = "Font.FontColor";
												- _Value = "0,0,0";
												- _Type = Color;
											}
											{ IProperty 
												- _Name = "Font.Size";
												- _Value = "10";
												- _Type = Int;
											}
											{ IProperty 
												- _Name = "Font.Weight@Child.NameCompartment@Name";
												- _Value = "$<cancel>";
												- _Type = Int;
											}
											{ IProperty 
												- _Name = "Line.LineColor";
												- _Value = "121,122,0";
												- _Type = Color;
											}
											{ IProperty 
												- _Name = "Line.LineWidth";
												- _Value = "0";
												- _Type = Int;
											}
										}
									}
								}
							}
						}
					}
					- m_type = 109;
					- m_pModelObject = { IHandle 
						- _m2Class = "IClassifierRole";
						- _id = GUID cf3f4e2c-480f-4939-aa9c-990e70f48ce7;
					}
					- m_pParent = GUID da6e79a0-5f33-4349-b105-cee25cf8f8f0;
					- m_name = { CGIText 
						- m_str = "Elevator[0]->lc:LoadController";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_drawBehavior = 0;
					- m_transform = 1 0 0 0.0536835 875 50 ;
					- m_bIsPreferencesInitialized = 0;
					- m_AdditionalLabel = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 1;
					}
					- m_position = 1 0 0  ;
					- m_pInheritsFrom = { IHandle 
						- _m2Class = "";
					}
					- m_nInheritanceMask = 0;
					- m_SubType = 0;
				}
				{ CGIMscColumnCR 
					- _id = GUID bdba7924-7191-4945-a431-b0c92e2650bb;
					- _properties = { IPropertyContainer 
						- Subjects = { IRPYRawContainer 
							- size = 1;
							- value = 
							{ IPropertySubject 
								- _Name = "Format";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "InstanceLine";
										- Properties = { IRPYRawContainer 
											- size = 8;
											- value = 
											{ IProperty 
												- _Name = "DefaultSize";
												- _Value = "0,0,96,437";
												- _Type = String;
											}
											{ IProperty 
												- _Name = "Fill.FillColor";
												- _Value = "255,255,255";
												- _Type = Color;
											}
											{ IProperty 
												- _Name = "Font.Font";
												- _Value = "Arial";
												- _Type = String;
											}
											{ IProperty 
												- _Name = "Font.FontColor";
												- _Value = "0,0,0";
												- _Type = Color;
											}
											{ IProperty 
												- _Name = "Font.Size";
												- _Value = "10";
												- _Type = Int;
											}
											{ IProperty 
												- _Name = "Font.Weight@Child.NameCompartment@Name";
												- _Value = "$<cancel>";
												- _Type = Int;
											}
											{ IProperty 
												- _Name = "Line.LineColor";
												- _Value = "121,122,0";
												- _Type = Color;
											}
											{ IProperty 
												- _Name = "Line.LineWidth";
												- _Value = "0";
												- _Type = Int;
											}
										}
									}
								}
							}
						}
					}
					- m_type = 109;
					- m_pModelObject = { IHandle 
						- _m2Class = "IClassifierRole";
						- _id = GUID 4b08cd87-ee84-44f4-8fb9-da864c6ffcd4;
					}
					- m_pParent = GUID da6e79a0-5f33-4349-b105-cee25cf8f8f0;
					- m_name = { CGIText 
						- m_str = "Elevator[0]->mc:MoveController";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_drawBehavior = 0;
					- m_transform = 1 0 0 0.0536835 769 50 ;
					- m_bIsPreferencesInitialized = 0;
					- m_AdditionalLabel = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 1;
					}
					- m_position = 1 0 0  ;
					- m_pInheritsFrom = { IHandle 
						- _m2Class = "";
					}
					- m_nInheritanceMask = 0;
					- m_SubType = 0;
				}
				{ CGIMscColumnCR 
					- _id = GUID 4e331a03-e87e-431c-bb19-a9e8ca930ff6;
					- _properties = { IPropertyContainer 
						- Subjects = { IRPYRawContainer 
							- size = 1;
							- value = 
							{ IPropertySubject 
								- _Name = "Format";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "InstanceLine";
										- Properties = { IRPYRawContainer 
											- size = 8;
											- value = 
											{ IProperty 
												- _Name = "DefaultSize";
												- _Value = "0,0,96,437";
												- _Type = String;
											}
											{ IProperty 
												- _Name = "Fill.FillColor";
												- _Value = "255,255,255";
												- _Type = Color;
											}
											{ IProperty 
												- _Name = "Font.Font";
												- _Value = "Arial";
												- _Type = String;
											}
											{ IProperty 
												- _Name = "Font.FontColor";
												- _Value = "0,0,0";
												- _Type = Color;
											}
											{ IProperty 
												- _Name = "Font.Size";
												- _Value = "10";
												- _Type = Int;
											}
											{ IProperty 
												- _Name = "Font.Weight@Child.NameCompartment@Name";
												- _Value = "$<cancel>";
												- _Type = Int;
											}
											{ IProperty 
												- _Name = "Line.LineColor";
												- _Value = "121,122,0";
												- _Type = Color;
											}
											{ IProperty 
												- _Name = "Line.LineWidth";
												- _Value = "0";
												- _Type = Int;
											}
										}
									}
								}
							}
						}
					}
					- m_type = 109;
					- m_pModelObject = { IHandle 
						- _m2Class = "IClassifierRole";
						- _id = GUID 336cdd56-7224-4069-8900-dd6fc0c71b48;
					}
					- m_pParent = GUID da6e79a0-5f33-4349-b105-cee25cf8f8f0;
					- m_name = { CGIText 
						- m_str = "Elevator[0]->rc:ReadyController";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_drawBehavior = 0;
					- m_transform = 1 0 0 0.0536835 981 50 ;
					- m_bIsPreferencesInitialized = 0;
					- m_AdditionalLabel = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 1;
					}
					- m_position = 1 0 0  ;
					- m_pInheritsFrom = { IHandle 
						- _m2Class = "";
					}
					- m_nInheritanceMask = 0;
					- m_SubType = 0;
				}
				{ CGIMscColumnCR 
					- _id = GUID 8765da51-df7e-4d8d-8407-1e0939deacc0;
					- _properties = { IPropertyContainer 
						- Subjects = { IRPYRawContainer 
							- size = 1;
							- value = 
							{ IPropertySubject 
								- _Name = "Format";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "InstanceLine";
										- Properties = { IRPYRawContainer 
											- size = 8;
											- value = 
											{ IProperty 
												- _Name = "DefaultSize";
												- _Value = "0,0,96,437";
												- _Type = String;
											}
											{ IProperty 
												- _Name = "Fill.FillColor";
												- _Value = "255,255,255";
												- _Type = Color;
											}
											{ IProperty 
												- _Name = "Font.Font";
												- _Value = "Arial";
												- _Type = String;
											}
											{ IProperty 
												- _Name = "Font.FontColor";
												- _Value = "0,0,0";
												- _Type = Color;
											}
											{ IProperty 
												- _Name = "Font.Size";
												- _Value = "10";
												- _Type = Int;
											}
											{ IProperty 
												- _Name = "Font.Weight@Child.NameCompartment@Name";
												- _Value = "$<cancel>";
												- _Type = Int;
											}
											{ IProperty 
												- _Name = "Line.LineColor";
												- _Value = "121,122,0";
												- _Type = Color;
											}
											{ IProperty 
												- _Name = "Line.LineWidth";
												- _Value = "0";
												- _Type = Int;
											}
										}
									}
								}
							}
						}
					}
					- m_type = 109;
					- m_pModelObject = { IHandle 
						- _m2Class = "IClassifierRole";
						- _id = GUID 783378b5-c9a0-49a9-8227-235f77509f55;
					}
					- m_pParent = GUID da6e79a0-5f33-4349-b105-cee25cf8f8f0;
					- m_name = { CGIText 
						- m_str = "Elevator[0]->hc->en:Engine";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_drawBehavior = 0;
					- m_transform = 1 0 0 0.0536835 383 50 ;
					- m_bIsPreferencesInitialized = 0;
					- m_AdditionalLabel = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 1;
					}
					- m_position = 1 0 0  ;
					- m_pInheritsFrom = { IHandle 
						- _m2Class = "";
					}
					- m_nInheritanceMask = 0;
					- m_SubType = 0;
				}
				{ CGIMscConditionMark 
					- _id = GUID 4525d0f7-eb1d-4a47-a8da-880188b93451;
					- m_type = 114;
					- m_pModelObject = { IHandle 
						- _m2Class = "IMessage";
						- _id = GUID 048d0642-bcdf-49f4-99bb-18216a5e43f3;
					}
					- m_pParent = GUID c6e227c0-ac5c-4c36-90c6-47536000dd70;
					- m_name = { CGIText 
						- m_str = "Waiting";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_drawBehavior = 4096;
					- m_transform = 1.14286 0 0 18.6277 0 1192.17 ;
					- m_bIsPreferencesInitialized = 1;
					- m_polygon = 4 0 0  0 51  84 51  84 0  ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
					- Compartments = { IRPYRawContainer 
						- size = 0;
					}
				}
				{ CGIMscConditionMark 
					- _id = GUID 7ca84ec1-dee7-461a-8c98-eaccf1045194;
					- m_type = 114;
					- m_pModelObject = { IHandle 
						- _m2Class = "IMessage";
						- _id = GUID c1710611-3d85-4a95-86b0-a43175766573;
					}
					- m_pParent = GUID 8765da51-df7e-4d8d-8407-1e0939deacc0;
					- m_name = { CGIText 
						- m_str = "NotWorking";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_drawBehavior = 4096;
					- m_transform = 1.14286 0 0 18.6277 0 2514.74 ;
					- m_bIsPreferencesInitialized = 1;
					- m_polygon = 4 0 0  0 51  84 51  84 0  ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
					- Compartments = { IRPYRawContainer 
						- size = 0;
					}
				}
				{ CGIMscConditionMark 
					- _id = GUID c55925e5-37cc-484c-b2c6-ad6763414274;
					- m_type = 114;
					- m_pModelObject = { IHandle 
						- _m2Class = "IMessage";
						- _id = GUID cb29b00d-139d-4d69-a5ba-8674ccf11cda;
					}
					- m_pParent = GUID 74159e86-6131-425a-8cba-5fc6a6fd9a97;
					- m_name = { CGIText 
						- m_str = "Init";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_drawBehavior = 4096;
					- m_transform = 1.14286 0 0 18.6277 0 3837.31 ;
					- m_bIsPreferencesInitialized = 1;
					- m_polygon = 4 0 0  0 51  84 51  84 0  ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
					- Compartments = { IRPYRawContainer 
						- size = 0;
					}
				}
				{ CGIMscConditionMark 
					- _id = GUID 35715d12-ae05-4dde-ad91-20ea6f42f7b1;
					- m_type = 114;
					- m_pModelObject = { IHandle 
						- _m2Class = "IMessage";
						- _id = GUID e8777213-24f7-49e2-9983-d214a5cb3237;
					}
					- m_pParent = GUID 4394cf84-e62e-4673-8a0e-c83d75aa0c18;
					- m_name = { CGIText 
						- m_str = "Waiting";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_drawBehavior = 4096;
					- m_transform = 1.14286 0 0 18.6277 0 5159.88 ;
					- m_bIsPreferencesInitialized = 1;
					- m_polygon = 4 0 0  0 51  84 51  84 0  ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
					- Compartments = { IRPYRawContainer 
						- size = 0;
					}
				}
				{ CGIMscConditionMark 
					- _id = GUID dff16248-8d26-46f6-8b06-8241df763589;
					- m_type = 114;
					- m_pModelObject = { IHandle 
						- _m2Class = "IMessage";
						- _id = GUID b36e21cc-523c-45d0-933b-9a9fa992a8e5;
					}
					- m_pParent = GUID bdba7924-7191-4945-a431-b0c92e2650bb;
					- m_name = { CGIText 
						- m_str = "Init";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_drawBehavior = 4096;
					- m_transform = 1.14286 0 0 18.6277 0 6482.44 ;
					- m_bIsPreferencesInitialized = 1;
					- m_polygon = 4 0 0  0 51  84 51  84 0  ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
					- Compartments = { IRPYRawContainer 
						- size = 0;
					}
				}
				{ CGIMscConditionMark 
					- _id = GUID 5831f7e7-07b6-47b4-9197-854729faf288;
					- m_type = 114;
					- m_pModelObject = { IHandle 
						- _m2Class = "IMessage";
						- _id = GUID 542cbd4f-68ec-4646-8413-fe08a914c5fa;
					}
					- m_pParent = GUID 4e331a03-e87e-431c-bb19-a9e8ca930ff6;
					- m_name = { CGIText 
						- m_str = "Init";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_drawBehavior = 4096;
					- m_transform = 1.14286 0 0 18.6277 0 7805.01 ;
					- m_bIsPreferencesInitialized = 1;
					- m_polygon = 4 0 0  0 51  84 51  84 0  ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
					- Compartments = { IRPYRawContainer 
						- size = 0;
					}
				}
				{ CGIMscConditionMark 
					- _id = GUID 5621c743-226e-4a18-98ab-523561edc1b1;
					- m_type = 114;
					- m_pModelObject = { IHandle 
						- _m2Class = "IMessage";
						- _id = GUID 8e57ba4e-0f8b-4f52-96f3-8acb08a0a87e;
					}
					- m_pParent = GUID 8ee83f03-e542-49ea-9ca7-be0a407d6529;
					- m_name = { CGIText 
						- m_str = "EmergencyStopped";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_drawBehavior = 4096;
					- m_transform = 1.14286 0 0 18.6277 0 9127.58 ;
					- m_bIsPreferencesInitialized = 1;
					- m_polygon = 4 0 0  0 51  84 51  84 0  ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
					- Compartments = { IRPYRawContainer 
						- size = 0;
					}
				}
				{ CGIMscConditionMark 
					- _id = GUID 4f761db1-5dd0-4d3f-a07f-a7f65dec562d;
					- m_type = 114;
					- m_pModelObject = { IHandle 
						- _m2Class = "IMessage";
						- _id = GUID 587b08e9-fa98-4b7e-90f3-9dd858bfdd0a;
					}
					- m_pParent = GUID 8ee83f03-e542-49ea-9ca7-be0a407d6529;
					- m_name = { CGIText 
						- m_str = "waitingForRequest";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_drawBehavior = 4096;
					- m_transform = 1.14286 0 0 18.6277 0 10450.1 ;
					- m_bIsPreferencesInitialized = 1;
					- m_polygon = 4 0 0  0 51  84 51  84 0  ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
					- Compartments = { IRPYRawContainer 
						- size = 0;
					}
				}
				{ CGIMscConditionMark 
					- _id = GUID 44f458d9-e62e-4577-a810-016425955eec;
					- m_type = 114;
					- m_pModelObject = { IHandle 
						- _m2Class = "IMessage";
						- _id = GUID 90fdc9fa-e782-432d-87b9-f0eb54b15de1;
					}
					- m_pParent = GUID 8ee83f03-e542-49ea-9ca7-be0a407d6529;
					- m_name = { CGIText 
						- m_str = "Moving";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_drawBehavior = 4096;
					- m_transform = 1.14286 0 0 18.6277 0 11772.7 ;
					- m_bIsPreferencesInitialized = 1;
					- m_polygon = 4 0 0  0 51  84 51  84 0  ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
					- Compartments = { IRPYRawContainer 
						- size = 0;
					}
				}
				{ CGIMscMessage 
					- _id = GUID fcd230e2-ad8e-43a1-b5c4-19e428e7fc7b;
					- _properties = { IPropertyContainer 
						- Subjects = { IRPYRawContainer 
							- size = 1;
							- value = 
							{ IPropertySubject 
								- _Name = "Format";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "Message";
										- Properties = { IRPYRawContainer 
											- size = 2;
											- value = 
											{ IProperty 
												- _Name = "Line.LineStyle";
												- _Value = "0";
												- _Type = Int;
											}
											{ IProperty 
												- _Name = "Line.LineWidth";
												- _Value = "1";
												- _Type = Int;
											}
										}
									}
								}
							}
						}
					}
					- m_type = 110;
					- m_pModelObject = { IHandle 
						- _m2Class = "IMessage";
						- _id = GUID 18a1711b-b586-457f-9736-b217abfbe640;
					}
					- m_pParent = ;
					- m_name = { CGIText 
						- m_str = "MoveControllerE(level = 1)";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 6;
					}
					- m_drawBehavior = 4096;
					- m_bIsPreferencesInitialized = 1;
					- m_pSource = GUID 8ee83f03-e542-49ea-9ca7-be0a407d6529;
					- m_sourceType = 'F';
					- m_pTarget = GUID 74159e86-6131-425a-8cba-5fc6a6fd9a97;
					- m_targetType = 'T';
					- m_direction = ' ';
					- m_rpn = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_anglePoint1 = 0 0 ;
					- m_anglePoint2 = 0 0 ;
					- m_line_style = 0;
					- m_SourcePort = 48 13207 ;
					- m_TargetPort = 48 13580 ;
					- m_bLeft = 0;
				}
				{ CGIMscConditionMark 
					- _id = GUID df125085-b7f6-43f2-86f2-ff16c5fc3fa8;
					- m_type = 114;
					- m_pModelObject = { IHandle 
						- _m2Class = "IMessage";
						- _id = GUID 98c38fb9-a39d-4e0e-8b57-8c436e89985b;
					}
					- m_pParent = GUID 74159e86-6131-425a-8cba-5fc6a6fd9a97;
					- m_name = { CGIText 
						- m_str = "MovingDecision";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_drawBehavior = 4096;
					- m_transform = 1.14286 0 0 18.6277 0 13840.4 ;
					- m_bIsPreferencesInitialized = 1;
					- m_polygon = 4 0 0  0 51  84 51  84 0  ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
					- Compartments = { IRPYRawContainer 
						- size = 0;
					}
				}
				{ CGIMscMessage 
					- _id = GUID 071b504b-5b17-44a7-926c-3b7d670c4e67;
					- _properties = { IPropertyContainer 
						- Subjects = { IRPYRawContainer 
							- size = 1;
							- value = 
							{ IPropertySubject 
								- _Name = "Format";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "Message";
										- Properties = { IRPYRawContainer 
											- size = 2;
											- value = 
											{ IProperty 
												- _Name = "Line.LineStyle";
												- _Value = "0";
												- _Type = Int;
											}
											{ IProperty 
												- _Name = "Line.LineWidth";
												- _Value = "1";
												- _Type = Int;
											}
										}
									}
								}
							}
						}
					}
					- m_type = 110;
					- m_pModelObject = { IHandle 
						- _m2Class = "IMessage";
						- _id = GUID e0bfbcec-8178-44fa-ae4c-5082fe7a986f;
					}
					- m_pParent = ;
					- m_name = { CGIText 
						- m_str = "Up()";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 6;
					}
					- m_drawBehavior = 4096;
					- m_bIsPreferencesInitialized = 1;
					- m_pSource = GUID 74159e86-6131-425a-8cba-5fc6a6fd9a97;
					- m_sourceType = 'F';
					- m_pTarget = GUID 8765da51-df7e-4d8d-8407-1e0939deacc0;
					- m_targetType = 'T';
					- m_direction = ' ';
					- m_rpn = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_anglePoint1 = 0 0 ;
					- m_anglePoint2 = 0 0 ;
					- m_line_style = 0;
					- m_SourcePort = 48 15275 ;
					- m_TargetPort = 48 17249 ;
					- m_bLeft = 0;
				}
				{ CGIMscConditionMark 
					- _id = GUID 249d99b8-338f-4526-92fe-e7cdb8ba1d92;
					- m_type = 114;
					- m_pModelObject = { IHandle 
						- _m2Class = "IMessage";
						- _id = GUID f147f189-5b74-4670-a7fa-cac36cf7d1f9;
					}
					- m_pParent = GUID 74159e86-6131-425a-8cba-5fc6a6fd9a97;
					- m_name = { CGIText 
						- m_str = "BeforeWaitingForEvent";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_drawBehavior = 4096;
					- m_transform = 1.14286 0 0 24.1064 0 15535.5 ;
					- m_bIsPreferencesInitialized = 1;
					- m_polygon = 4 0 0  0 51  84 51  84 0  ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
					- Compartments = { IRPYRawContainer 
						- size = 0;
					}
				}
				{ CGIMscConditionMark 
					- _id = GUID b057cb09-9198-4a5a-8bd0-db4fa9e2dccc;
					- m_type = 114;
					- m_pModelObject = { IHandle 
						- _m2Class = "IMessage";
						- _id = GUID 7fff4b72-58ac-4e30-bfb7-cb73fed036cc;
					}
					- m_pParent = GUID 8765da51-df7e-4d8d-8407-1e0939deacc0;
					- m_name = { CGIText 
						- m_str = "accepteventaction_2";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_drawBehavior = 4096;
					- m_transform = 1.14286 0 0 18.6277 0 17510 ;
					- m_bIsPreferencesInitialized = 1;
					- m_polygon = 4 0 0  0 51  84 51  84 0  ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
					- Compartments = { IRPYRawContainer 
						- size = 0;
					}
				}
				{ CGIMscMessage 
					- _id = GUID d83d3c17-4a94-4047-87ca-a8bb6aa94d36;
					- m_type = 115;
					- m_pModelObject = { IHandle 
						- _m2Class = "IMessage";
						- _id = GUID a8899f5d-f49e-42ab-8a8e-a85a3fda0c70;
					}
					- m_pParent = ;
					- m_name = { CGIText 
						- m_str = "tm(2000) at ROOT.state_5.accepteventaction_2";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 6;
					}
					- m_drawBehavior = 4096;
					- m_bIsPreferencesInitialized = 1;
					- m_pSource = GUID 8765da51-df7e-4d8d-8407-1e0939deacc0;
					- m_sourceType = 'F';
					- m_pTarget = GUID 8765da51-df7e-4d8d-8407-1e0939deacc0;
					- m_targetType = 'T';
					- m_direction = ' ';
					- m_rpn = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_arrow = 2 461 1067  461 1087  ;
					- m_anglePoint1 = 0 0 ;
					- m_anglePoint2 = 0 0 ;
					- m_line_style = 2;
					- m_SourcePort = 48 18944 ;
					- m_TargetPort = 48 19317 ;
					- m_bLeft = 0;
				}
				{ CGIMscMessage 
					- _id = GUID bf89fb31-2cb2-43ce-9638-d9ab403364b1;
					- _properties = { IPropertyContainer 
						- Subjects = { IRPYRawContainer 
							- size = 1;
							- value = 
							{ IPropertySubject 
								- _Name = "Format";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "Message";
										- Properties = { IRPYRawContainer 
											- size = 2;
											- value = 
											{ IProperty 
												- _Name = "Line.LineStyle";
												- _Value = "0";
												- _Type = Int;
											}
											{ IProperty 
												- _Name = "Line.LineWidth";
												- _Value = "1";
												- _Type = Int;
											}
										}
									}
								}
							}
						}
					}
					- m_type = 110;
					- m_pModelObject = { IHandle 
						- _m2Class = "IMessage";
						- _id = GUID 3df88de4-79c8-4133-86b4-b1a879ad9d90;
					}
					- m_pParent = ;
					- m_name = { CGIText 
						- m_str = "Up()";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 4;
					}
					- m_drawBehavior = 4096;
					- m_bIsPreferencesInitialized = 1;
					- m_pSource = GUID 8765da51-df7e-4d8d-8407-1e0939deacc0;
					- m_sourceType = 'F';
					- m_pTarget = GUID 74159e86-6131-425a-8cba-5fc6a6fd9a97;
					- m_targetType = 'T';
					- m_direction = ' ';
					- m_rpn = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_anglePoint1 = 0 0 ;
					- m_anglePoint2 = 0 0 ;
					- m_line_style = 0;
					- m_SourcePort = 48 19689 ;
					- m_TargetPort = 48 21385 ;
					- m_bLeft = 0;
				}
				{ CGIMscConditionMark 
					- _id = GUID 38e95244-6012-47a5-a0a8-8c612574e20d;
					- m_type = 114;
					- m_pModelObject = { IHandle 
						- _m2Class = "IMessage";
						- _id = GUID 5b5199dc-259b-4cf3-ad83-8338007a1c4e;
					}
					- m_pParent = GUID 8765da51-df7e-4d8d-8407-1e0939deacc0;
					- m_name = { CGIText 
						- m_str = "NotWorking";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_drawBehavior = 4096;
					- m_transform = 1.14286 0 0 18.6277 0 19950.3 ;
					- m_bIsPreferencesInitialized = 1;
					- m_polygon = 4 0 0  0 51  84 51  84 0  ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
					- Compartments = { IRPYRawContainer 
						- size = 0;
					}
				}
				{ CGIMscConditionMark 
					- _id = GUID 6fea786a-e37a-4d27-9057-93b3f06288c0;
					- m_type = 114;
					- m_pModelObject = { IHandle 
						- _m2Class = "IMessage";
						- _id = GUID 4f0756ad-e6a3-4705-a9fa-3b762ef34bfc;
					}
					- m_pParent = GUID 74159e86-6131-425a-8cba-5fc6a6fd9a97;
					- m_name = { CGIText 
						- m_str = "MovingDecision";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_drawBehavior = 4096;
					- m_transform = 1.14286 0 0 18.6277 0 21645.4 ;
					- m_bIsPreferencesInitialized = 1;
					- m_polygon = 4 0 0  0 51  84 51  84 0  ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
					- Compartments = { IRPYRawContainer 
						- size = 0;
					}
				}
				{ CGIMscMessage 
					- _id = GUID 4e158927-c772-42d6-a2ff-2e3a5e90bb3a;
					- _properties = { IPropertyContainer 
						- Subjects = { IRPYRawContainer 
							- size = 1;
							- value = 
							{ IPropertySubject 
								- _Name = "Format";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "Message";
										- Properties = { IRPYRawContainer 
											- size = 2;
											- value = 
											{ IProperty 
												- _Name = "Line.LineStyle";
												- _Value = "0";
												- _Type = Int;
											}
											{ IProperty 
												- _Name = "Line.LineWidth";
												- _Value = "1";
												- _Type = Int;
											}
										}
									}
								}
							}
						}
					}
					- m_type = 110;
					- m_pModelObject = { IHandle 
						- _m2Class = "IMessage";
						- _id = GUID 57077a9b-1bb2-42eb-9d8a-91569416d6e7;
					}
					- m_pParent = ;
					- m_name = { CGIText 
						- m_str = "Up()";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 6;
					}
					- m_drawBehavior = 4096;
					- m_bIsPreferencesInitialized = 1;
					- m_pSource = GUID 74159e86-6131-425a-8cba-5fc6a6fd9a97;
					- m_sourceType = 'F';
					- m_pTarget = GUID 8765da51-df7e-4d8d-8407-1e0939deacc0;
					- m_targetType = 'T';
					- m_direction = ' ';
					- m_rpn = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_anglePoint1 = 0 0 ;
					- m_anglePoint2 = 0 0 ;
					- m_line_style = 0;
					- m_SourcePort = 48 23080 ;
					- m_TargetPort = 48 25054 ;
					- m_bLeft = 0;
				}
				{ CGIMscConditionMark 
					- _id = GUID f245f49b-ca16-4d34-aec8-fa194a8b8729;
					- m_type = 114;
					- m_pModelObject = { IHandle 
						- _m2Class = "IMessage";
						- _id = GUID bcdd98b2-22be-4646-a744-936f0fc59fb7;
					}
					- m_pParent = GUID 74159e86-6131-425a-8cba-5fc6a6fd9a97;
					- m_name = { CGIText 
						- m_str = "BeforeWaitingForEvent";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_drawBehavior = 4096;
					- m_transform = 1.14286 0 0 24.1064 0 23340.5 ;
					- m_bIsPreferencesInitialized = 1;
					- m_polygon = 4 0 0  0 51  84 51  84 0  ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
					- Compartments = { IRPYRawContainer 
						- size = 0;
					}
				}
				{ CGIMscConditionMark 
					- _id = GUID 583c5ee3-b747-474e-93b7-96558509921e;
					- m_type = 114;
					- m_pModelObject = { IHandle 
						- _m2Class = "IMessage";
						- _id = GUID 0aa0a36a-6bee-40b2-99b7-1160e5b763cc;
					}
					- m_pParent = GUID 8765da51-df7e-4d8d-8407-1e0939deacc0;
					- m_name = { CGIText 
						- m_str = "accepteventaction_2";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_drawBehavior = 4096;
					- m_transform = 1.14286 0 0 18.6277 0 25315.1 ;
					- m_bIsPreferencesInitialized = 1;
					- m_polygon = 4 0 0  0 51  84 51  84 0  ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
					- Compartments = { IRPYRawContainer 
						- size = 0;
					}
				}
				{ CGIMscMessage 
					- _id = GUID c9a21838-f940-4540-9784-0f8c8f45782f;
					- _properties = { IPropertyContainer 
						- Subjects = { IRPYRawContainer 
							- size = 1;
							- value = 
							{ IPropertySubject 
								- _Name = "Format";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "Message";
										- Properties = { IRPYRawContainer 
											- size = 2;
											- value = 
											{ IProperty 
												- _Name = "Line.LineStyle";
												- _Value = "0";
												- _Type = Int;
											}
											{ IProperty 
												- _Name = "Line.LineWidth";
												- _Value = "1";
												- _Type = Int;
											}
										}
									}
								}
							}
						}
					}
					- m_type = 110;
					- m_pModelObject = { IHandle 
						- _m2Class = "IMessage";
						- _id = GUID 0e6a7d2d-4de5-48e1-b426-cb181b871775;
					}
					- m_pParent = ;
					- m_name = { CGIText 
						- m_str = "Stop()";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 6;
					}
					- m_drawBehavior = 4096;
					- m_bIsPreferencesInitialized = 1;
					- m_pSource = GUID 8ee83f03-e542-49ea-9ca7-be0a407d6529;
					- m_sourceType = 'F';
					- m_pTarget = GUID 74159e86-6131-425a-8cba-5fc6a6fd9a97;
					- m_targetType = 'T';
					- m_direction = ' ';
					- m_rpn = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_anglePoint1 = 0 0 ;
					- m_anglePoint2 = 0 0 ;
					- m_line_style = 0;
					- m_SourcePort = 48 26749 ;
					- m_TargetPort = 48 28445 ;
					- m_bLeft = 0;
				}
				{ CGIMscConditionMark 
					- _id = GUID dcbbe9df-021a-41a6-82ad-27954d8f1b4d;
					- m_type = 114;
					- m_pModelObject = { IHandle 
						- _m2Class = "IMessage";
						- _id = GUID 55613d73-5886-4dc9-aaf9-dd8a3c021c4a;
					}
					- m_pParent = GUID 8ee83f03-e542-49ea-9ca7-be0a407d6529;
					- m_name = { CGIText 
						- m_str = "EmergencyStopped";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_drawBehavior = 4096;
					- m_transform = 1.14286 0 0 18.6277 0 27010.2 ;
					- m_bIsPreferencesInitialized = 1;
					- m_polygon = 4 0 0  0 51  84 51  84 0  ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
					- Compartments = { IRPYRawContainer 
						- size = 0;
					}
				}
				{ CGIMscConditionMark 
					- _id = GUID 96cea6bb-21ce-458a-b711-ed597e947943;
					- m_type = 114;
					- m_pModelObject = { IHandle 
						- _m2Class = "IMessage";
						- _id = GUID 55831158-806f-4ce6-9b71-8a2b43653b1d;
					}
					- m_pParent = GUID 74159e86-6131-425a-8cba-5fc6a6fd9a97;
					- m_name = { CGIText 
						- m_str = "Init";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_drawBehavior = 4096;
					- m_transform = 1.14286 0 0 18.6277 0 28705.3 ;
					- m_bIsPreferencesInitialized = 1;
					- m_polygon = 4 0 0  0 51  84 51  84 0  ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
					- Compartments = { IRPYRawContainer 
						- size = 0;
					}
				}
				{ CGIMscMessage 
					- _id = GUID 2f36f919-dc88-4971-a517-1592c66ccf1d;
					- m_type = 115;
					- m_pModelObject = { IHandle 
						- _m2Class = "IMessage";
						- _id = GUID 50ace297-cb3d-471b-892c-6c08915f2cf7;
					}
					- m_pParent = ;
					- m_name = { CGIText 
						- m_str = "tm(2000) at ROOT.state_5.accepteventaction_2";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 6;
					}
					- m_drawBehavior = 4096;
					- m_bIsPreferencesInitialized = 1;
					- m_pSource = GUID 8765da51-df7e-4d8d-8407-1e0939deacc0;
					- m_sourceType = 'F';
					- m_pTarget = GUID 8765da51-df7e-4d8d-8407-1e0939deacc0;
					- m_targetType = 'T';
					- m_direction = ' ';
					- m_rpn = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_arrow = 2 461 1668  461 1688  ;
					- m_anglePoint1 = 0 0 ;
					- m_anglePoint2 = 0 0 ;
					- m_line_style = 2;
					- m_SourcePort = 48 30140 ;
					- m_TargetPort = 48 30512 ;
					- m_bLeft = 0;
				}
				{ CGIMscMessage 
					- _id = GUID c14188ee-65ab-47f4-bb44-4ccaf56a68a9;
					- _properties = { IPropertyContainer 
						- Subjects = { IRPYRawContainer 
							- size = 1;
							- value = 
							{ IPropertySubject 
								- _Name = "Format";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "Message";
										- Properties = { IRPYRawContainer 
											- size = 2;
											- value = 
											{ IProperty 
												- _Name = "Line.LineStyle";
												- _Value = "0";
												- _Type = Int;
											}
											{ IProperty 
												- _Name = "Line.LineWidth";
												- _Value = "1";
												- _Type = Int;
											}
										}
									}
								}
							}
						}
					}
					- m_type = 110;
					- m_pModelObject = { IHandle 
						- _m2Class = "IMessage";
						- _id = GUID ef02c74d-8c6e-418a-84b1-8e290617e1e8;
					}
					- m_pParent = ;
					- m_name = { CGIText 
						- m_str = "Up()";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 4;
					}
					- m_drawBehavior = 4096;
					- m_bIsPreferencesInitialized = 1;
					- m_pSource = GUID 8765da51-df7e-4d8d-8407-1e0939deacc0;
					- m_sourceType = 'F';
					- m_pTarget = GUID 74159e86-6131-425a-8cba-5fc6a6fd9a97;
					- m_targetType = 'T';
					- m_direction = ' ';
					- m_rpn = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_anglePoint1 = 0 0 ;
					- m_anglePoint2 = 0 0 ;
					- m_line_style = 0;
					- m_SourcePort = 48 30885 ;
					- m_TargetPort = 48 32580 ;
					- m_bLeft = 0;
				}
				{ CGIMscConditionMark 
					- _id = GUID d749ad5c-fc23-4eb0-b392-ae125b08de6a;
					- m_type = 114;
					- m_pModelObject = { IHandle 
						- _m2Class = "IMessage";
						- _id = GUID 7b6ffd4f-c6e0-4d28-94c0-c773b97e433f;
					}
					- m_pParent = GUID 8765da51-df7e-4d8d-8407-1e0939deacc0;
					- m_name = { CGIText 
						- m_str = "NotWorking";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_drawBehavior = 4096;
					- m_transform = 1.14286 0 0 18.6277 0 31145.5 ;
					- m_bIsPreferencesInitialized = 1;
					- m_polygon = 4 0 0  0 51  84 51  84 0  ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
					- Compartments = { IRPYRawContainer 
						- size = 0;
					}
				}
				{ CGIMscConditionMark 
					- _id = GUID 9c759af4-3c54-468b-a756-6781049db1ee;
					- m_type = 114;
					- m_pModelObject = { IHandle 
						- _m2Class = "IMessage";
						- _id = GUID 56a76a34-5d92-4c69-9455-0a2f162ddc29;
					}
					- m_pParent = GUID 8ee83f03-e542-49ea-9ca7-be0a407d6529;
					- m_name = { CGIText 
						- m_str = "EmergencyMoving";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_drawBehavior = 4096;
					- m_transform = 1.14286 0 0 18.6277 0 32840.6 ;
					- m_bIsPreferencesInitialized = 1;
					- m_polygon = 4 0 0  0 51  84 51  84 0  ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
					- Compartments = { IRPYRawContainer 
						- size = 0;
					}
				}
				{ CGIMscMessage 
					- _id = GUID 83e489bc-c848-49da-a28f-2ee227d6e153;
					- _properties = { IPropertyContainer 
						- Subjects = { IRPYRawContainer 
							- size = 1;
							- value = 
							{ IPropertySubject 
								- _Name = "Format";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "Message";
										- Properties = { IRPYRawContainer 
											- size = 2;
											- value = 
											{ IProperty 
												- _Name = "Line.LineStyle";
												- _Value = "0";
												- _Type = Int;
											}
											{ IProperty 
												- _Name = "Line.LineWidth";
												- _Value = "1";
												- _Type = Int;
											}
										}
									}
								}
							}
						}
					}
					- m_type = 110;
					- m_pModelObject = { IHandle 
						- _m2Class = "IMessage";
						- _id = GUID 00059f90-b985-40b3-aab6-89da21e1696e;
					}
					- m_pParent = ;
					- m_name = { CGIText 
						- m_str = "MoveControllerE(level = 0)";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 6;
					}
					- m_drawBehavior = 4096;
					- m_bIsPreferencesInitialized = 1;
					- m_pSource = GUID 8ee83f03-e542-49ea-9ca7-be0a407d6529;
					- m_sourceType = 'F';
					- m_pTarget = GUID 74159e86-6131-425a-8cba-5fc6a6fd9a97;
					- m_targetType = 'T';
					- m_direction = ' ';
					- m_rpn = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_anglePoint1 = 0 0 ;
					- m_anglePoint2 = 0 0 ;
					- m_line_style = 0;
					- m_SourcePort = 48 34275 ;
					- m_TargetPort = 48 34648 ;
					- m_bLeft = 0;
				}
				{ CGIMscConditionMark 
					- _id = GUID 54c6453a-dfdd-4652-9385-92930d1412a3;
					- m_type = 114;
					- m_pModelObject = { IHandle 
						- _m2Class = "IMessage";
						- _id = GUID 4c5a6f19-421c-446c-a78f-63f9161b94c3;
					}
					- m_pParent = GUID 74159e86-6131-425a-8cba-5fc6a6fd9a97;
					- m_name = { CGIText 
						- m_str = "MovingDecision";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_drawBehavior = 4096;
					- m_transform = 1.14286 0 0 18.6277 0 34908.3 ;
					- m_bIsPreferencesInitialized = 1;
					- m_polygon = 4 0 0  0 51  84 51  84 0  ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
					- Compartments = { IRPYRawContainer 
						- size = 0;
					}
				}
				{ CGIMscMessage 
					- _id = GUID 997a17f2-7eb3-472d-ad26-a4d88db8d079;
					- _properties = { IPropertyContainer 
						- Subjects = { IRPYRawContainer 
							- size = 1;
							- value = 
							{ IPropertySubject 
								- _Name = "Format";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "Message";
										- Properties = { IRPYRawContainer 
											- size = 2;
											- value = 
											{ IProperty 
												- _Name = "Line.LineStyle";
												- _Value = "0";
												- _Type = Int;
											}
											{ IProperty 
												- _Name = "Line.LineWidth";
												- _Value = "1";
												- _Type = Int;
											}
										}
									}
								}
							}
						}
					}
					- m_type = 110;
					- m_pModelObject = { IHandle 
						- _m2Class = "IMessage";
						- _id = GUID c5a5bd1e-6cf5-4753-ab5e-859f5dda51c6;
					}
					- m_pParent = ;
					- m_name = { CGIText 
						- m_str = "Down()";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 6;
					}
					- m_drawBehavior = 4096;
					- m_bIsPreferencesInitialized = 1;
					- m_pSource = GUID 74159e86-6131-425a-8cba-5fc6a6fd9a97;
					- m_sourceType = 'F';
					- m_pTarget = GUID 8765da51-df7e-4d8d-8407-1e0939deacc0;
					- m_targetType = 'T';
					- m_direction = ' ';
					- m_rpn = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_anglePoint1 = 0 0 ;
					- m_anglePoint2 = 0 0 ;
					- m_line_style = 0;
					- m_SourcePort = 48 36343 ;
					- m_TargetPort = 48 38317 ;
					- m_bLeft = 0;
				}
				{ CGIMscConditionMark 
					- _id = GUID bb6d9598-93a7-47c2-8a68-385cacdd90af;
					- m_type = 114;
					- m_pModelObject = { IHandle 
						- _m2Class = "IMessage";
						- _id = GUID 66c3a03e-5ac4-4f29-a56f-ec716922737e;
					}
					- m_pParent = GUID 74159e86-6131-425a-8cba-5fc6a6fd9a97;
					- m_name = { CGIText 
						- m_str = "BeforeWaitingForEvent";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_drawBehavior = 4096;
					- m_transform = 1.14286 0 0 24.1064 0 36603.4 ;
					- m_bIsPreferencesInitialized = 1;
					- m_polygon = 4 0 0  0 51  84 51  84 0  ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
					- Compartments = { IRPYRawContainer 
						- size = 0;
					}
				}
				{ CGIMscConditionMark 
					- _id = GUID 8a8a6a88-7409-4362-b5ac-4a3afea7cc5b;
					- m_type = 114;
					- m_pModelObject = { IHandle 
						- _m2Class = "IMessage";
						- _id = GUID 64297161-1352-4e56-9d4c-74dae44f31f5;
					}
					- m_pParent = GUID 8765da51-df7e-4d8d-8407-1e0939deacc0;
					- m_name = { CGIText 
						- m_str = "accepteventaction_1";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_drawBehavior = 4096;
					- m_transform = 1.14286 0 0 18.6277 0 38578 ;
					- m_bIsPreferencesInitialized = 1;
					- m_polygon = 4 0 0  0 51  84 51  84 0  ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
					- Compartments = { IRPYRawContainer 
						- size = 0;
					}
				}
				{ CGIMscMessage 
					- _id = GUID bc9a1596-eae0-4a60-9219-c5270a074419;
					- m_type = 115;
					- m_pModelObject = { IHandle 
						- _m2Class = "IMessage";
						- _id = GUID e44cf4e0-41c5-4a8a-8b3d-51db55d5e2a4;
					}
					- m_pParent = ;
					- m_name = { CGIText 
						- m_str = "tm(2000) at ROOT.state_5.accepteventaction_1";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 6;
					}
					- m_drawBehavior = 4096;
					- m_bIsPreferencesInitialized = 1;
					- m_pSource = GUID 8765da51-df7e-4d8d-8407-1e0939deacc0;
					- m_sourceType = 'F';
					- m_pTarget = GUID 8765da51-df7e-4d8d-8407-1e0939deacc0;
					- m_targetType = 'T';
					- m_direction = ' ';
					- m_rpn = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_arrow = 2 461 2198  461 2218  ;
					- m_anglePoint1 = 0 0 ;
					- m_anglePoint2 = 0 0 ;
					- m_line_style = 2;
					- m_SourcePort = 48 40012 ;
					- m_TargetPort = 48 40385 ;
					- m_bLeft = 0;
				}
				{ CGIMscMessage 
					- _id = GUID 79e63dd0-b0c5-4bec-a7ba-375bb1a9813f;
					- _properties = { IPropertyContainer 
						- Subjects = { IRPYRawContainer 
							- size = 1;
							- value = 
							{ IPropertySubject 
								- _Name = "Format";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "Message";
										- Properties = { IRPYRawContainer 
											- size = 2;
											- value = 
											{ IProperty 
												- _Name = "Line.LineStyle";
												- _Value = "0";
												- _Type = Int;
											}
											{ IProperty 
												- _Name = "Line.LineWidth";
												- _Value = "1";
												- _Type = Int;
											}
										}
									}
								}
							}
						}
					}
					- m_type = 110;
					- m_pModelObject = { IHandle 
						- _m2Class = "IMessage";
						- _id = GUID b093ee04-acd3-40cd-b867-d244b42ac21b;
					}
					- m_pParent = ;
					- m_name = { CGIText 
						- m_str = "Down()";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 4;
					}
					- m_drawBehavior = 4096;
					- m_bIsPreferencesInitialized = 1;
					- m_pSource = GUID 8765da51-df7e-4d8d-8407-1e0939deacc0;
					- m_sourceType = 'F';
					- m_pTarget = GUID 74159e86-6131-425a-8cba-5fc6a6fd9a97;
					- m_targetType = 'T';
					- m_direction = ' ';
					- m_rpn = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_anglePoint1 = 0 0 ;
					- m_anglePoint2 = 0 0 ;
					- m_line_style = 0;
					- m_SourcePort = 48 40757 ;
					- m_TargetPort = 48 42453 ;
					- m_bLeft = 0;
				}
				{ CGIMscConditionMark 
					- _id = GUID 0609090a-a8d9-48e4-a447-d6b5051546fb;
					- m_type = 114;
					- m_pModelObject = { IHandle 
						- _m2Class = "IMessage";
						- _id = GUID 9e7f27ec-d7dc-4d8a-8305-07038b89d95f;
					}
					- m_pParent = GUID 8765da51-df7e-4d8d-8407-1e0939deacc0;
					- m_name = { CGIText 
						- m_str = "NotWorking";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_drawBehavior = 4096;
					- m_transform = 1.14286 0 0 18.6277 0 41018.2 ;
					- m_bIsPreferencesInitialized = 1;
					- m_polygon = 4 0 0  0 51  84 51  84 0  ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
					- Compartments = { IRPYRawContainer 
						- size = 0;
					}
				}
				{ CGIMscConditionMark 
					- _id = GUID 755b439e-17d7-4ae9-a343-837494605544;
					- m_type = 114;
					- m_pModelObject = { IHandle 
						- _m2Class = "IMessage";
						- _id = GUID 71db86f5-478c-4fe6-97a8-2d3c27a58d0e;
					}
					- m_pParent = GUID 74159e86-6131-425a-8cba-5fc6a6fd9a97;
					- m_name = { CGIText 
						- m_str = "MovingDecision";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_drawBehavior = 4096;
					- m_transform = 1.14286 0 0 18.6277 0 42713.3 ;
					- m_bIsPreferencesInitialized = 1;
					- m_polygon = 4 0 0  0 51  84 51  84 0  ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
					- Compartments = { IRPYRawContainer 
						- size = 0;
					}
				}
				{ CGIMscConditionMark 
					- _id = GUID 9627d069-0247-4d3c-bca4-fb99451f750d;
					- m_type = 114;
					- m_pModelObject = { IHandle 
						- _m2Class = "IMessage";
						- _id = GUID bb0c49f7-dfbc-4f42-af0b-1cee8b6725a2;
					}
					- m_pParent = GUID 74159e86-6131-425a-8cba-5fc6a6fd9a97;
					- m_name = { CGIText 
						- m_str = "SendEvent";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_drawBehavior = 4096;
					- m_transform = 1.14286 0 0 18.6277 0 44035.9 ;
					- m_bIsPreferencesInitialized = 1;
					- m_polygon = 4 0 0  0 51  84 51  84 0  ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
					- Compartments = { IRPYRawContainer 
						- size = 0;
					}
				}
				{ CGIMscMessage 
					- _id = GUID ae5e6106-cdc0-4a96-8e31-1bd7d95ab64f;
					- _properties = { IPropertyContainer 
						- Subjects = { IRPYRawContainer 
							- size = 1;
							- value = 
							{ IPropertySubject 
								- _Name = "Format";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "Message";
										- Properties = { IRPYRawContainer 
											- size = 2;
											- value = 
											{ IProperty 
												- _Name = "Line.LineStyle";
												- _Value = "0";
												- _Type = Int;
											}
											{ IProperty 
												- _Name = "Line.LineWidth";
												- _Value = "1";
												- _Type = Int;
											}
										}
									}
								}
							}
						}
					}
					- m_type = 110;
					- m_pModelObject = { IHandle 
						- _m2Class = "IMessage";
						- _id = GUID 13b2f242-51fa-4c28-bc55-72d90833accf;
					}
					- m_pParent = ;
					- m_name = { CGIText 
						- m_str = "LevelController()";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 4;
					}
					- m_drawBehavior = 4096;
					- m_bIsPreferencesInitialized = 1;
					- m_pSource = GUID 74159e86-6131-425a-8cba-5fc6a6fd9a97;
					- m_sourceType = 'F';
					- m_pTarget = GUID 8ee83f03-e542-49ea-9ca7-be0a407d6529;
					- m_targetType = 'T';
					- m_direction = ' ';
					- m_rpn = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_anglePoint1 = 0 0 ;
					- m_anglePoint2 = 0 0 ;
					- m_line_style = 0;
					- m_SourcePort = 48 45470 ;
					- m_TargetPort = 48 45843 ;
					- m_bLeft = 0;
				}
				{ CGIMscConditionMark 
					- _id = GUID 80442f4c-0107-49f1-afb4-9ef9adb6724c;
					- m_type = 114;
					- m_pModelObject = { IHandle 
						- _m2Class = "IMessage";
						- _id = GUID b32f9644-ff59-4b7e-a40d-d9a9566122b3;
					}
					- m_pParent = GUID 8ee83f03-e542-49ea-9ca7-be0a407d6529;
					- m_name = { CGIText 
						- m_str = "EmergencyBaseLevel";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_drawBehavior = 4096;
					- m_transform = 1.14286 0 0 24.1064 0 46103.6 ;
					- m_bIsPreferencesInitialized = 1;
					- m_polygon = 4 0 0  0 51  84 51  84 0  ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
					- Compartments = { IRPYRawContainer 
						- size = 0;
					}
				}
				
				- m_access = 'Z';
				- m_modified = 'N';
				- m_fileVersion = "";
				- m_nModifyDate = 0;
				- m_nCreateDate = 0;
				- m_creator = "";
				- m_bScaleWithZoom = 1;
				- m_arrowStyle = 'S';
				- m_pRoot = GUID da6e79a0-5f33-4349-b105-cee25cf8f8f0;
				- m_currentLeftTop = 0 0 ;
				- m_currentRightBottom = 0 0 ;
			}
			- _defaultSubsystem = { IHandle 
				- _m2Class = "ISubsystem";
				- _filename = "Default.sbs";
				- _subsystem = "";
				- _class = "";
				- _name = "Default";
				- _id = GUID 2970263e-bdf6-4006-ba3e-12cef9acae52;
			}
			- m_pICollaboration = { ICollaboration 
				- _id = GUID 4adbd3f9-f1ef-4bcd-834c-36d32cc8e86d;
				- _modifiedTimeWeak = 1.1.1970::1:0:0;
				- ClassifierRoles = { IRPYRawContainer 
					- size = 11;
					- value = 
					{ IClassifierRole 
						- _id = GUID d512c32f-f665-410c-bc5c-c268d0c64648;
						- _name = "Elevator[0]->dc";
						- _modifiedTimeWeak = 1.2.1990::0:0:0;
						- m_eRoleType = CLASS;
						- m_pBase = { IHandle 
							- _m2Class = "IClass";
							- _filename = "Default.sbs";
							- _subsystem = "Default";
							- _class = "";
							- _name = "DoorsController";
							- _id = GUID 38aec46c-a896-46bc-bad4-16c77e5569d0;
						}
						- m_instance = { IHandle 
							- _m2Class = "";
						}
					}
					{ IClassifierRole 
						- _id = GUID d3a77353-9933-4ff7-b408-56cd6622e5ea;
						- _name = "Elevator[0]";
						- _modifiedTimeWeak = 1.2.1990::0:0:0;
						- m_eRoleType = CLASS;
						- m_pBase = { IHandle 
							- _m2Class = "IClass";
							- _filename = "Default.sbs";
							- _subsystem = "Default";
							- _class = "";
							- _name = "Elevator";
							- _id = GUID 6e9ca01c-040b-4e85-bbc9-4f7798db5ef4;
						}
						- m_instance = { IHandle 
							- _m2Class = "";
						}
					}
					{ IClassifierRole 
						- _id = GUID d0944990-686e-4a73-93d5-65d76ec5dcd6;
						- _name = "Elevator[0]->fl[0]";
						- _modifiedTimeWeak = 1.2.1990::0:0:0;
						- m_eRoleType = CLASS;
						- m_pBase = { IHandle 
							- _m2Class = "IClass";
							- _filename = "Default.sbs";
							- _subsystem = "Default";
							- _class = "";
							- _name = "Floor";
							- _id = GUID 7270c741-82dd-4d79-a637-77a3d1fb86d5;
						}
						- m_instance = { IHandle 
							- _m2Class = "";
						}
					}
					{ IClassifierRole 
						- _id = GUID 9adab9c6-343b-4de1-9c8b-935b366c3626;
						- _name = "Elevator[0]->fl[1]";
						- _modifiedTimeWeak = 1.2.1990::0:0:0;
						- m_eRoleType = CLASS;
						- m_pBase = { IHandle 
							- _m2Class = "IClass";
							- _filename = "Default.sbs";
							- _subsystem = "Default";
							- _class = "";
							- _name = "Floor";
							- _id = GUID 7270c741-82dd-4d79-a637-77a3d1fb86d5;
						}
						- m_instance = { IHandle 
							- _m2Class = "";
						}
					}
					{ IClassifierRole 
						- _id = GUID 49ff505d-fb89-490d-9cf2-db66b92be4e4;
						- _name = "Elevator[0]->fl[2]";
						- _modifiedTimeWeak = 1.2.1990::0:0:0;
						- m_eRoleType = CLASS;
						- m_pBase = { IHandle 
							- _m2Class = "IClass";
							- _filename = "Default.sbs";
							- _subsystem = "Default";
							- _class = "";
							- _name = "Floor";
							- _id = GUID 7270c741-82dd-4d79-a637-77a3d1fb86d5;
						}
						- m_instance = { IHandle 
							- _m2Class = "";
						}
					}
					{ IClassifierRole 
						- _id = GUID f0ff936f-4f00-4f41-a160-4d217f0d6276;
						- _name = "Elevator[0]->fl[3]";
						- _modifiedTimeWeak = 1.2.1990::0:0:0;
						- m_eRoleType = CLASS;
						- m_pBase = { IHandle 
							- _m2Class = "IClass";
							- _filename = "Default.sbs";
							- _subsystem = "Default";
							- _class = "";
							- _name = "Floor";
							- _id = GUID 7270c741-82dd-4d79-a637-77a3d1fb86d5;
						}
						- m_instance = { IHandle 
							- _m2Class = "";
						}
					}
					{ IClassifierRole 
						- _id = GUID b6b00713-6e03-4ec0-95ab-f01b5db15738;
						- _name = "Elevator[0]->hc";
						- _modifiedTimeWeak = 1.2.1990::0:0:0;
						- m_eRoleType = CLASS;
						- m_pBase = { IHandle 
							- _m2Class = "IClass";
							- _filename = "Default.sbs";
							- _subsystem = "Default";
							- _class = "";
							- _name = "HeightController";
							- _id = GUID 33dfe780-1e75-49ee-9e55-834dc5fafe51;
						}
						- m_instance = { IHandle 
							- _m2Class = "";
						}
					}
					{ IClassifierRole 
						- _id = GUID cf3f4e2c-480f-4939-aa9c-990e70f48ce7;
						- _name = "Elevator[0]->lc";
						- _modifiedTimeWeak = 1.2.1990::0:0:0;
						- m_eRoleType = CLASS;
						- m_pBase = { IHandle 
							- _m2Class = "IClass";
							- _filename = "Default.sbs";
							- _subsystem = "Default";
							- _class = "";
							- _name = "LoadController";
							- _id = GUID d1dd4690-acd6-41ad-8f2a-b8600ecd3f36;
						}
						- m_instance = { IHandle 
							- _m2Class = "";
						}
					}
					{ IClassifierRole 
						- _id = GUID 4b08cd87-ee84-44f4-8fb9-da864c6ffcd4;
						- _name = "Elevator[0]->mc";
						- _modifiedTimeWeak = 1.2.1990::0:0:0;
						- m_eRoleType = CLASS;
						- m_pBase = { IHandle 
							- _m2Class = "IClass";
							- _filename = "Default.sbs";
							- _subsystem = "Default";
							- _class = "";
							- _name = "MoveController";
							- _id = GUID d88479c4-1e3a-4ccb-8784-cfe96908d02b;
						}
						- m_instance = { IHandle 
							- _m2Class = "";
						}
					}
					{ IClassifierRole 
						- _id = GUID 336cdd56-7224-4069-8900-dd6fc0c71b48;
						- _name = "Elevator[0]->rc";
						- _modifiedTimeWeak = 1.2.1990::0:0:0;
						- m_eRoleType = CLASS;
						- m_pBase = { IHandle 
							- _m2Class = "IClass";
							- _filename = "Default.sbs";
							- _subsystem = "Default";
							- _class = "";
							- _name = "ReadyController";
							- _id = GUID 953be687-ea04-4796-b2b4-1ac0aa636051;
						}
						- m_instance = { IHandle 
							- _m2Class = "";
						}
					}
					{ IClassifierRole 
						- _id = GUID 783378b5-c9a0-49a9-8227-235f77509f55;
						- _name = "Elevator[0]->hc->en";
						- _modifiedTimeWeak = 1.2.1990::0:0:0;
						- m_eRoleType = CLASS;
						- m_pBase = { IHandle 
							- _m2Class = "IClass";
							- _filename = "Default.sbs";
							- _subsystem = "Default";
							- _class = "";
							- _name = "Engine";
							- _id = GUID 0fbd8080-b925-4cf0-8f63-7d60c45a83ce;
						}
						- m_instance = { IHandle 
							- _m2Class = "";
						}
					}
				}
				- Messages = { IRPYRawContainer 
					- size = 40;
					- value = 
					{ IMessage 
						- _id = GUID 048d0642-bcdf-49f4-99bb-18216a5e43f3;
						- _properties = { IPropertyContainer 
							- Subjects = { IRPYRawContainer 
								- size = 1;
								- value = 
								{ IPropertySubject 
									- _Name = "SequenceDiagram";
									- Metaclasses = { IRPYRawContainer 
										- size = 1;
										- value = 
										{ IPropertyMetaclass 
											- _Name = "Condition_Mark";
											- Properties = { IRPYRawContainer 
												- size = 1;
												- value = 
												{ IProperty 
													- _Name = "IsStateCondition";
													- _Value = "True";
													- _Type = Bool;
												}
											}
										}
									}
								}
							}
						}
						- _name = "connector";
						- _modifiedTimeWeak = 1.1.1970::1:0:0;
						- m_szSequence = "";
						- m_szActualArgs = "";
						- m_szReturnVal = "";
						- m_freeText = "Waiting";
						- m_pCommunicationConnection = { IHandle 
							- _m2Class = "";
						}
						- m_pReceiver = { IHandle 
							- _m2Class = "IClassifierRole";
							- _id = GUID d512c32f-f665-410c-bc5c-c268d0c64648;
						}
						- m_pSender = { IHandle 
							- _m2Class = "IClassifierRole";
							- _id = GUID d512c32f-f665-410c-bc5c-c268d0c64648;
						}
						- m_pFormalMessage = { IHandle 
							- _m2Class = "";
						}
						- m_eType = CONDITION;
						- m_targetExec = { IHandle 
							- _m2Class = "";
						}
						- m_srcExec = { IHandle 
							- _m2Class = "";
						}
					}
					{ IMessage 
						- _id = GUID c1710611-3d85-4a95-86b0-a43175766573;
						- _properties = { IPropertyContainer 
							- Subjects = { IRPYRawContainer 
								- size = 1;
								- value = 
								{ IPropertySubject 
									- _Name = "SequenceDiagram";
									- Metaclasses = { IRPYRawContainer 
										- size = 1;
										- value = 
										{ IPropertyMetaclass 
											- _Name = "Condition_Mark";
											- Properties = { IRPYRawContainer 
												- size = 1;
												- value = 
												{ IProperty 
													- _Name = "IsStateCondition";
													- _Value = "True";
													- _Type = Bool;
												}
											}
										}
									}
								}
							}
						}
						- _name = "connector";
						- _modifiedTimeWeak = 1.1.1970::1:0:0;
						- m_szSequence = "";
						- m_szActualArgs = "";
						- m_szReturnVal = "";
						- m_freeText = "NotWorking";
						- m_pCommunicationConnection = { IHandle 
							- _m2Class = "";
						}
						- m_pReceiver = { IHandle 
							- _m2Class = "IClassifierRole";
							- _id = GUID 783378b5-c9a0-49a9-8227-235f77509f55;
						}
						- m_pSender = { IHandle 
							- _m2Class = "IClassifierRole";
							- _id = GUID 783378b5-c9a0-49a9-8227-235f77509f55;
						}
						- m_pFormalMessage = { IHandle 
							- _m2Class = "";
						}
						- m_eType = CONDITION;
						- m_targetExec = { IHandle 
							- _m2Class = "";
						}
						- m_srcExec = { IHandle 
							- _m2Class = "";
						}
					}
					{ IMessage 
						- _id = GUID cb29b00d-139d-4d69-a5ba-8674ccf11cda;
						- _properties = { IPropertyContainer 
							- Subjects = { IRPYRawContainer 
								- size = 1;
								- value = 
								{ IPropertySubject 
									- _Name = "SequenceDiagram";
									- Metaclasses = { IRPYRawContainer 
										- size = 1;
										- value = 
										{ IPropertyMetaclass 
											- _Name = "Condition_Mark";
											- Properties = { IRPYRawContainer 
												- size = 1;
												- value = 
												{ IProperty 
													- _Name = "IsStateCondition";
													- _Value = "True";
													- _Type = Bool;
												}
											}
										}
									}
								}
							}
						}
						- _name = "connector";
						- _modifiedTimeWeak = 1.1.1970::1:0:0;
						- m_szSequence = "";
						- m_szActualArgs = "";
						- m_szReturnVal = "";
						- m_freeText = "Init";
						- m_pCommunicationConnection = { IHandle 
							- _m2Class = "";
						}
						- m_pReceiver = { IHandle 
							- _m2Class = "IClassifierRole";
							- _id = GUID b6b00713-6e03-4ec0-95ab-f01b5db15738;
						}
						- m_pSender = { IHandle 
							- _m2Class = "IClassifierRole";
							- _id = GUID b6b00713-6e03-4ec0-95ab-f01b5db15738;
						}
						- m_pFormalMessage = { IHandle 
							- _m2Class = "";
						}
						- m_eType = CONDITION;
						- m_targetExec = { IHandle 
							- _m2Class = "";
						}
						- m_srcExec = { IHandle 
							- _m2Class = "";
						}
					}
					{ IMessage 
						- _id = GUID e8777213-24f7-49e2-9983-d214a5cb3237;
						- _properties = { IPropertyContainer 
							- Subjects = { IRPYRawContainer 
								- size = 1;
								- value = 
								{ IPropertySubject 
									- _Name = "SequenceDiagram";
									- Metaclasses = { IRPYRawContainer 
										- size = 1;
										- value = 
										{ IPropertyMetaclass 
											- _Name = "Condition_Mark";
											- Properties = { IRPYRawContainer 
												- size = 1;
												- value = 
												{ IProperty 
													- _Name = "IsStateCondition";
													- _Value = "True";
													- _Type = Bool;
												}
											}
										}
									}
								}
							}
						}
						- _name = "connector";
						- _modifiedTimeWeak = 1.1.1970::1:0:0;
						- m_szSequence = "";
						- m_szActualArgs = "";
						- m_szReturnVal = "";
						- m_freeText = "Waiting";
						- m_pCommunicationConnection = { IHandle 
							- _m2Class = "";
						}
						- m_pReceiver = { IHandle 
							- _m2Class = "IClassifierRole";
							- _id = GUID cf3f4e2c-480f-4939-aa9c-990e70f48ce7;
						}
						- m_pSender = { IHandle 
							- _m2Class = "IClassifierRole";
							- _id = GUID cf3f4e2c-480f-4939-aa9c-990e70f48ce7;
						}
						- m_pFormalMessage = { IHandle 
							- _m2Class = "";
						}
						- m_eType = CONDITION;
						- m_targetExec = { IHandle 
							- _m2Class = "";
						}
						- m_srcExec = { IHandle 
							- _m2Class = "";
						}
					}
					{ IMessage 
						- _id = GUID b36e21cc-523c-45d0-933b-9a9fa992a8e5;
						- _properties = { IPropertyContainer 
							- Subjects = { IRPYRawContainer 
								- size = 1;
								- value = 
								{ IPropertySubject 
									- _Name = "SequenceDiagram";
									- Metaclasses = { IRPYRawContainer 
										- size = 1;
										- value = 
										{ IPropertyMetaclass 
											- _Name = "Condition_Mark";
											- Properties = { IRPYRawContainer 
												- size = 1;
												- value = 
												{ IProperty 
													- _Name = "IsStateCondition";
													- _Value = "True";
													- _Type = Bool;
												}
											}
										}
									}
								}
							}
						}
						- _name = "connector";
						- _modifiedTimeWeak = 1.1.1970::1:0:0;
						- m_szSequence = "";
						- m_szActualArgs = "";
						- m_szReturnVal = "";
						- m_freeText = "Init";
						- m_pCommunicationConnection = { IHandle 
							- _m2Class = "";
						}
						- m_pReceiver = { IHandle 
							- _m2Class = "IClassifierRole";
							- _id = GUID 4b08cd87-ee84-44f4-8fb9-da864c6ffcd4;
						}
						- m_pSender = { IHandle 
							- _m2Class = "IClassifierRole";
							- _id = GUID 4b08cd87-ee84-44f4-8fb9-da864c6ffcd4;
						}
						- m_pFormalMessage = { IHandle 
							- _m2Class = "";
						}
						- m_eType = CONDITION;
						- m_targetExec = { IHandle 
							- _m2Class = "";
						}
						- m_srcExec = { IHandle 
							- _m2Class = "";
						}
					}
					{ IMessage 
						- _id = GUID 542cbd4f-68ec-4646-8413-fe08a914c5fa;
						- _properties = { IPropertyContainer 
							- Subjects = { IRPYRawContainer 
								- size = 1;
								- value = 
								{ IPropertySubject 
									- _Name = "SequenceDiagram";
									- Metaclasses = { IRPYRawContainer 
										- size = 1;
										- value = 
										{ IPropertyMetaclass 
											- _Name = "Condition_Mark";
											- Properties = { IRPYRawContainer 
												- size = 1;
												- value = 
												{ IProperty 
													- _Name = "IsStateCondition";
													- _Value = "True";
													- _Type = Bool;
												}
											}
										}
									}
								}
							}
						}
						- _name = "connector";
						- _modifiedTimeWeak = 1.1.1970::1:0:0;
						- m_szSequence = "";
						- m_szActualArgs = "";
						- m_szReturnVal = "";
						- m_freeText = "Init";
						- m_pCommunicationConnection = { IHandle 
							- _m2Class = "";
						}
						- m_pReceiver = { IHandle 
							- _m2Class = "IClassifierRole";
							- _id = GUID 336cdd56-7224-4069-8900-dd6fc0c71b48;
						}
						- m_pSender = { IHandle 
							- _m2Class = "IClassifierRole";
							- _id = GUID 336cdd56-7224-4069-8900-dd6fc0c71b48;
						}
						- m_pFormalMessage = { IHandle 
							- _m2Class = "";
						}
						- m_eType = CONDITION;
						- m_targetExec = { IHandle 
							- _m2Class = "";
						}
						- m_srcExec = { IHandle 
							- _m2Class = "";
						}
					}
					{ IMessage 
						- _id = GUID 8e57ba4e-0f8b-4f52-96f3-8acb08a0a87e;
						- _properties = { IPropertyContainer 
							- Subjects = { IRPYRawContainer 
								- size = 1;
								- value = 
								{ IPropertySubject 
									- _Name = "SequenceDiagram";
									- Metaclasses = { IRPYRawContainer 
										- size = 1;
										- value = 
										{ IPropertyMetaclass 
											- _Name = "Condition_Mark";
											- Properties = { IRPYRawContainer 
												- size = 1;
												- value = 
												{ IProperty 
													- _Name = "IsStateCondition";
													- _Value = "True";
													- _Type = Bool;
												}
											}
										}
									}
								}
							}
						}
						- _name = "connector";
						- _modifiedTimeWeak = 1.1.1970::1:0:0;
						- m_szSequence = "";
						- m_szActualArgs = "";
						- m_szReturnVal = "";
						- m_freeText = "EmergencyStopped";
						- m_pCommunicationConnection = { IHandle 
							- _m2Class = "";
						}
						- m_pReceiver = { IHandle 
							- _m2Class = "IClassifierRole";
							- _id = GUID d3a77353-9933-4ff7-b408-56cd6622e5ea;
						}
						- m_pSender = { IHandle 
							- _m2Class = "IClassifierRole";
							- _id = GUID d3a77353-9933-4ff7-b408-56cd6622e5ea;
						}
						- m_pFormalMessage = { IHandle 
							- _m2Class = "";
						}
						- m_eType = CONDITION;
						- m_targetExec = { IHandle 
							- _m2Class = "";
						}
						- m_srcExec = { IHandle 
							- _m2Class = "";
						}
					}
					{ IMessage 
						- _id = GUID 587b08e9-fa98-4b7e-90f3-9dd858bfdd0a;
						- _properties = { IPropertyContainer 
							- Subjects = { IRPYRawContainer 
								- size = 1;
								- value = 
								{ IPropertySubject 
									- _Name = "SequenceDiagram";
									- Metaclasses = { IRPYRawContainer 
										- size = 1;
										- value = 
										{ IPropertyMetaclass 
											- _Name = "Condition_Mark";
											- Properties = { IRPYRawContainer 
												- size = 1;
												- value = 
												{ IProperty 
													- _Name = "IsStateCondition";
													- _Value = "True";
													- _Type = Bool;
												}
											}
										}
									}
								}
							}
						}
						- _name = "connector";
						- _modifiedTimeWeak = 1.1.1970::1:0:0;
						- m_szSequence = "";
						- m_szActualArgs = "";
						- m_szReturnVal = "";
						- m_freeText = "waitingForRequest";
						- m_pCommunicationConnection = { IHandle 
							- _m2Class = "";
						}
						- m_pReceiver = { IHandle 
							- _m2Class = "IClassifierRole";
							- _id = GUID d3a77353-9933-4ff7-b408-56cd6622e5ea;
						}
						- m_pSender = { IHandle 
							- _m2Class = "IClassifierRole";
							- _id = GUID d3a77353-9933-4ff7-b408-56cd6622e5ea;
						}
						- m_pFormalMessage = { IHandle 
							- _m2Class = "";
						}
						- m_eType = CONDITION;
						- m_targetExec = { IHandle 
							- _m2Class = "";
						}
						- m_srcExec = { IHandle 
							- _m2Class = "";
						}
					}
					{ IMessage 
						- _id = GUID 90fdc9fa-e782-432d-87b9-f0eb54b15de1;
						- _properties = { IPropertyContainer 
							- Subjects = { IRPYRawContainer 
								- size = 1;
								- value = 
								{ IPropertySubject 
									- _Name = "SequenceDiagram";
									- Metaclasses = { IRPYRawContainer 
										- size = 1;
										- value = 
										{ IPropertyMetaclass 
											- _Name = "Condition_Mark";
											- Properties = { IRPYRawContainer 
												- size = 1;
												- value = 
												{ IProperty 
													- _Name = "IsStateCondition";
													- _Value = "True";
													- _Type = Bool;
												}
											}
										}
									}
								}
							}
						}
						- _name = "connector";
						- _modifiedTimeWeak = 1.1.1970::1:0:0;
						- m_szSequence = "";
						- m_szActualArgs = "";
						- m_szReturnVal = "";
						- m_freeText = "Moving";
						- m_pCommunicationConnection = { IHandle 
							- _m2Class = "";
						}
						- m_pReceiver = { IHandle 
							- _m2Class = "IClassifierRole";
							- _id = GUID d3a77353-9933-4ff7-b408-56cd6622e5ea;
						}
						- m_pSender = { IHandle 
							- _m2Class = "IClassifierRole";
							- _id = GUID d3a77353-9933-4ff7-b408-56cd6622e5ea;
						}
						- m_pFormalMessage = { IHandle 
							- _m2Class = "";
						}
						- m_eType = CONDITION;
						- m_targetExec = { IHandle 
							- _m2Class = "";
						}
						- m_srcExec = { IHandle 
							- _m2Class = "";
						}
					}
					{ IMessage 
						- _id = GUID 18a1711b-b586-457f-9736-b217abfbe640;
						- _myState = 8192;
						- _name = "MoveControllerE";
						- _modifiedTimeWeak = 1.1.1970::1:0:0;
						- m_szSequence = "1.";
						- m_szActualArgs = "level = 1";
						- m_szReturnVal = "";
						- m_pCommunicationConnection = { IHandle 
							- _m2Class = "";
						}
						- m_pReceiver = { IHandle 
							- _m2Class = "IClassifierRole";
							- _id = GUID b6b00713-6e03-4ec0-95ab-f01b5db15738;
						}
						- m_pSender = { IHandle 
							- _m2Class = "IClassifierRole";
							- _id = GUID d3a77353-9933-4ff7-b408-56cd6622e5ea;
						}
						- m_pFormalMessage = { IHandle 
							- _m2Class = "IEvent";
							- _filename = "Default.sbs";
							- _subsystem = "Default";
							- _class = "";
							- _name = "MoveControllerE(int)";
							- _id = GUID 41513545-4957-4be8-9307-dcf62835f390;
						}
						- m_eType = EVENT;
						- m_targetExec = { IHandle 
							- _m2Class = "";
						}
						- m_srcExec = { IHandle 
							- _m2Class = "";
						}
					}
					{ IMessage 
						- _id = GUID 98c38fb9-a39d-4e0e-8b57-8c436e89985b;
						- _properties = { IPropertyContainer 
							- Subjects = { IRPYRawContainer 
								- size = 1;
								- value = 
								{ IPropertySubject 
									- _Name = "SequenceDiagram";
									- Metaclasses = { IRPYRawContainer 
										- size = 1;
										- value = 
										{ IPropertyMetaclass 
											- _Name = "Condition_Mark";
											- Properties = { IRPYRawContainer 
												- size = 1;
												- value = 
												{ IProperty 
													- _Name = "IsStateCondition";
													- _Value = "True";
													- _Type = Bool;
												}
											}
										}
									}
								}
							}
						}
						- _name = "connector";
						- _modifiedTimeWeak = 1.1.1970::1:0:0;
						- m_szSequence = "";
						- m_szActualArgs = "";
						- m_szReturnVal = "";
						- m_freeText = "MovingDecision";
						- m_pCommunicationConnection = { IHandle 
							- _m2Class = "";
						}
						- m_pReceiver = { IHandle 
							- _m2Class = "IClassifierRole";
							- _id = GUID b6b00713-6e03-4ec0-95ab-f01b5db15738;
						}
						- m_pSender = { IHandle 
							- _m2Class = "IClassifierRole";
							- _id = GUID b6b00713-6e03-4ec0-95ab-f01b5db15738;
						}
						- m_pFormalMessage = { IHandle 
							- _m2Class = "";
						}
						- m_eType = CONDITION;
						- m_targetExec = { IHandle 
							- _m2Class = "";
						}
						- m_srcExec = { IHandle 
							- _m2Class = "";
						}
					}
					{ IMessage 
						- _id = GUID e0bfbcec-8178-44fa-ae4c-5082fe7a986f;
						- _name = "Up";
						- _modifiedTimeWeak = 1.1.1970::1:0:0;
						- m_szSequence = "2.";
						- m_szActualArgs = "";
						- m_szReturnVal = "";
						- m_pCommunicationConnection = { IHandle 
							- _m2Class = "";
						}
						- m_pReceiver = { IHandle 
							- _m2Class = "IClassifierRole";
							- _id = GUID 783378b5-c9a0-49a9-8227-235f77509f55;
						}
						- m_pSender = { IHandle 
							- _m2Class = "IClassifierRole";
							- _id = GUID b6b00713-6e03-4ec0-95ab-f01b5db15738;
						}
						- m_pFormalMessage = { IHandle 
							- _m2Class = "IEvent";
							- _filename = "Default.sbs";
							- _subsystem = "Default";
							- _class = "";
							- _name = "Up()";
							- _id = GUID e55ee974-7a59-4354-be2d-5918a481dadf;
						}
						- m_eType = EVENT;
						- m_targetExec = { IHandle 
							- _m2Class = "";
						}
						- m_srcExec = { IHandle 
							- _m2Class = "";
						}
					}
					{ IMessage 
						- _id = GUID f147f189-5b74-4670-a7fa-cac36cf7d1f9;
						- _properties = { IPropertyContainer 
							- Subjects = { IRPYRawContainer 
								- size = 1;
								- value = 
								{ IPropertySubject 
									- _Name = "SequenceDiagram";
									- Metaclasses = { IRPYRawContainer 
										- size = 1;
										- value = 
										{ IPropertyMetaclass 
											- _Name = "Condition_Mark";
											- Properties = { IRPYRawContainer 
												- size = 1;
												- value = 
												{ IProperty 
													- _Name = "IsStateCondition";
													- _Value = "True";
													- _Type = Bool;
												}
											}
										}
									}
								}
							}
						}
						- _name = "connector";
						- _modifiedTimeWeak = 1.1.1970::1:0:0;
						- m_szSequence = "";
						- m_szActualArgs = "";
						- m_szReturnVal = "";
						- m_freeText = "BeforeWaitingForEvent";
						- m_pCommunicationConnection = { IHandle 
							- _m2Class = "";
						}
						- m_pReceiver = { IHandle 
							- _m2Class = "IClassifierRole";
							- _id = GUID b6b00713-6e03-4ec0-95ab-f01b5db15738;
						}
						- m_pSender = { IHandle 
							- _m2Class = "IClassifierRole";
							- _id = GUID b6b00713-6e03-4ec0-95ab-f01b5db15738;
						}
						- m_pFormalMessage = { IHandle 
							- _m2Class = "";
						}
						- m_eType = CONDITION;
						- m_targetExec = { IHandle 
							- _m2Class = "";
						}
						- m_srcExec = { IHandle 
							- _m2Class = "";
						}
					}
					{ IMessage 
						- _id = GUID 7fff4b72-58ac-4e30-bfb7-cb73fed036cc;
						- _properties = { IPropertyContainer 
							- Subjects = { IRPYRawContainer 
								- size = 1;
								- value = 
								{ IPropertySubject 
									- _Name = "SequenceDiagram";
									- Metaclasses = { IRPYRawContainer 
										- size = 1;
										- value = 
										{ IPropertyMetaclass 
											- _Name = "Condition_Mark";
											- Properties = { IRPYRawContainer 
												- size = 1;
												- value = 
												{ IProperty 
													- _Name = "IsStateCondition";
													- _Value = "True";
													- _Type = Bool;
												}
											}
										}
									}
								}
							}
						}
						- _name = "connector";
						- _modifiedTimeWeak = 1.1.1970::1:0:0;
						- m_szSequence = "";
						- m_szActualArgs = "";
						- m_szReturnVal = "";
						- m_freeText = "accepteventaction_2";
						- m_pCommunicationConnection = { IHandle 
							- _m2Class = "";
						}
						- m_pReceiver = { IHandle 
							- _m2Class = "IClassifierRole";
							- _id = GUID 783378b5-c9a0-49a9-8227-235f77509f55;
						}
						- m_pSender = { IHandle 
							- _m2Class = "IClassifierRole";
							- _id = GUID 783378b5-c9a0-49a9-8227-235f77509f55;
						}
						- m_pFormalMessage = { IHandle 
							- _m2Class = "";
						}
						- m_eType = CONDITION;
						- m_targetExec = { IHandle 
							- _m2Class = "";
						}
						- m_srcExec = { IHandle 
							- _m2Class = "";
						}
					}
					{ IMessage 
						- _id = GUID a8899f5d-f49e-42ab-8a8e-a85a3fda0c70;
						- _myState = 8192;
						- _name = "tm";
						- _modifiedTimeWeak = 1.1.1970::1:0:0;
						- m_szSequence = "3.";
						- m_szActualArgs = "2000";
						- m_szReturnVal = "";
						- m_freeText = " at ROOT.state_5.accepteventaction_2";
						- m_pCommunicationConnection = { IHandle 
							- _m2Class = "";
						}
						- m_pReceiver = { IHandle 
							- _m2Class = "IClassifierRole";
							- _id = GUID 783378b5-c9a0-49a9-8227-235f77509f55;
						}
						- m_pSender = { IHandle 
							- _m2Class = "IClassifierRole";
							- _id = GUID 783378b5-c9a0-49a9-8227-235f77509f55;
						}
						- m_pFormalMessage = { IHandle 
							- _m2Class = "";
						}
						- m_eType = TIMEOUT;
						- m_targetExec = { IHandle 
							- _m2Class = "";
						}
						- m_srcExec = { IHandle 
							- _m2Class = "";
						}
					}
					{ IMessage 
						- _id = GUID 3df88de4-79c8-4133-86b4-b1a879ad9d90;
						- _name = "Up";
						- _modifiedTimeWeak = 1.1.1970::1:0:0;
						- m_szSequence = "4.";
						- m_szActualArgs = "";
						- m_szReturnVal = "";
						- m_pCommunicationConnection = { IHandle 
							- _m2Class = "";
						}
						- m_pReceiver = { IHandle 
							- _m2Class = "IClassifierRole";
							- _id = GUID b6b00713-6e03-4ec0-95ab-f01b5db15738;
						}
						- m_pSender = { IHandle 
							- _m2Class = "IClassifierRole";
							- _id = GUID 783378b5-c9a0-49a9-8227-235f77509f55;
						}
						- m_pFormalMessage = { IHandle 
							- _m2Class = "IEvent";
							- _filename = "Default.sbs";
							- _subsystem = "Default";
							- _class = "";
							- _name = "Up()";
							- _id = GUID e55ee974-7a59-4354-be2d-5918a481dadf;
						}
						- m_eType = EVENT;
						- m_targetExec = { IHandle 
							- _m2Class = "";
						}
						- m_srcExec = { IHandle 
							- _m2Class = "";
						}
					}
					{ IMessage 
						- _id = GUID 5b5199dc-259b-4cf3-ad83-8338007a1c4e;
						- _properties = { IPropertyContainer 
							- Subjects = { IRPYRawContainer 
								- size = 1;
								- value = 
								{ IPropertySubject 
									- _Name = "SequenceDiagram";
									- Metaclasses = { IRPYRawContainer 
										- size = 1;
										- value = 
										{ IPropertyMetaclass 
											- _Name = "Condition_Mark";
											- Properties = { IRPYRawContainer 
												- size = 1;
												- value = 
												{ IProperty 
													- _Name = "IsStateCondition";
													- _Value = "True";
													- _Type = Bool;
												}
											}
										}
									}
								}
							}
						}
						- _name = "connector";
						- _modifiedTimeWeak = 1.1.1970::1:0:0;
						- m_szSequence = "";
						- m_szActualArgs = "";
						- m_szReturnVal = "";
						- m_freeText = "NotWorking";
						- m_pCommunicationConnection = { IHandle 
							- _m2Class = "";
						}
						- m_pReceiver = { IHandle 
							- _m2Class = "IClassifierRole";
							- _id = GUID 783378b5-c9a0-49a9-8227-235f77509f55;
						}
						- m_pSender = { IHandle 
							- _m2Class = "IClassifierRole";
							- _id = GUID 783378b5-c9a0-49a9-8227-235f77509f55;
						}
						- m_pFormalMessage = { IHandle 
							- _m2Class = "";
						}
						- m_eType = CONDITION;
						- m_targetExec = { IHandle 
							- _m2Class = "";
						}
						- m_srcExec = { IHandle 
							- _m2Class = "";
						}
					}
					{ IMessage 
						- _id = GUID 4f0756ad-e6a3-4705-a9fa-3b762ef34bfc;
						- _properties = { IPropertyContainer 
							- Subjects = { IRPYRawContainer 
								- size = 1;
								- value = 
								{ IPropertySubject 
									- _Name = "SequenceDiagram";
									- Metaclasses = { IRPYRawContainer 
										- size = 1;
										- value = 
										{ IPropertyMetaclass 
											- _Name = "Condition_Mark";
											- Properties = { IRPYRawContainer 
												- size = 1;
												- value = 
												{ IProperty 
													- _Name = "IsStateCondition";
													- _Value = "True";
													- _Type = Bool;
												}
											}
										}
									}
								}
							}
						}
						- _name = "connector";
						- _modifiedTimeWeak = 1.1.1970::1:0:0;
						- m_szSequence = "";
						- m_szActualArgs = "";
						- m_szReturnVal = "";
						- m_freeText = "MovingDecision";
						- m_pCommunicationConnection = { IHandle 
							- _m2Class = "";
						}
						- m_pReceiver = { IHandle 
							- _m2Class = "IClassifierRole";
							- _id = GUID b6b00713-6e03-4ec0-95ab-f01b5db15738;
						}
						- m_pSender = { IHandle 
							- _m2Class = "IClassifierRole";
							- _id = GUID b6b00713-6e03-4ec0-95ab-f01b5db15738;
						}
						- m_pFormalMessage = { IHandle 
							- _m2Class = "";
						}
						- m_eType = CONDITION;
						- m_targetExec = { IHandle 
							- _m2Class = "";
						}
						- m_srcExec = { IHandle 
							- _m2Class = "";
						}
					}
					{ IMessage 
						- _id = GUID 57077a9b-1bb2-42eb-9d8a-91569416d6e7;
						- _name = "Up";
						- _modifiedTimeWeak = 1.1.1970::1:0:0;
						- m_szSequence = "5.";
						- m_szActualArgs = "";
						- m_szReturnVal = "";
						- m_pCommunicationConnection = { IHandle 
							- _m2Class = "";
						}
						- m_pReceiver = { IHandle 
							- _m2Class = "IClassifierRole";
							- _id = GUID 783378b5-c9a0-49a9-8227-235f77509f55;
						}
						- m_pSender = { IHandle 
							- _m2Class = "IClassifierRole";
							- _id = GUID b6b00713-6e03-4ec0-95ab-f01b5db15738;
						}
						- m_pFormalMessage = { IHandle 
							- _m2Class = "IEvent";
							- _filename = "Default.sbs";
							- _subsystem = "Default";
							- _class = "";
							- _name = "Up()";
							- _id = GUID e55ee974-7a59-4354-be2d-5918a481dadf;
						}
						- m_eType = EVENT;
						- m_targetExec = { IHandle 
							- _m2Class = "";
						}
						- m_srcExec = { IHandle 
							- _m2Class = "";
						}
					}
					{ IMessage 
						- _id = GUID bcdd98b2-22be-4646-a744-936f0fc59fb7;
						- _properties = { IPropertyContainer 
							- Subjects = { IRPYRawContainer 
								- size = 1;
								- value = 
								{ IPropertySubject 
									- _Name = "SequenceDiagram";
									- Metaclasses = { IRPYRawContainer 
										- size = 1;
										- value = 
										{ IPropertyMetaclass 
											- _Name = "Condition_Mark";
											- Properties = { IRPYRawContainer 
												- size = 1;
												- value = 
												{ IProperty 
													- _Name = "IsStateCondition";
													- _Value = "True";
													- _Type = Bool;
												}
											}
										}
									}
								}
							}
						}
						- _name = "connector";
						- _modifiedTimeWeak = 1.1.1970::1:0:0;
						- m_szSequence = "";
						- m_szActualArgs = "";
						- m_szReturnVal = "";
						- m_freeText = "BeforeWaitingForEvent";
						- m_pCommunicationConnection = { IHandle 
							- _m2Class = "";
						}
						- m_pReceiver = { IHandle 
							- _m2Class = "IClassifierRole";
							- _id = GUID b6b00713-6e03-4ec0-95ab-f01b5db15738;
						}
						- m_pSender = { IHandle 
							- _m2Class = "IClassifierRole";
							- _id = GUID b6b00713-6e03-4ec0-95ab-f01b5db15738;
						}
						- m_pFormalMessage = { IHandle 
							- _m2Class = "";
						}
						- m_eType = CONDITION;
						- m_targetExec = { IHandle 
							- _m2Class = "";
						}
						- m_srcExec = { IHandle 
							- _m2Class = "";
						}
					}
					{ IMessage 
						- _id = GUID 0aa0a36a-6bee-40b2-99b7-1160e5b763cc;
						- _properties = { IPropertyContainer 
							- Subjects = { IRPYRawContainer 
								- size = 1;
								- value = 
								{ IPropertySubject 
									- _Name = "SequenceDiagram";
									- Metaclasses = { IRPYRawContainer 
										- size = 1;
										- value = 
										{ IPropertyMetaclass 
											- _Name = "Condition_Mark";
											- Properties = { IRPYRawContainer 
												- size = 1;
												- value = 
												{ IProperty 
													- _Name = "IsStateCondition";
													- _Value = "True";
													- _Type = Bool;
												}
											}
										}
									}
								}
							}
						}
						- _name = "connector";
						- _modifiedTimeWeak = 1.1.1970::1:0:0;
						- m_szSequence = "";
						- m_szActualArgs = "";
						- m_szReturnVal = "";
						- m_freeText = "accepteventaction_2";
						- m_pCommunicationConnection = { IHandle 
							- _m2Class = "";
						}
						- m_pReceiver = { IHandle 
							- _m2Class = "IClassifierRole";
							- _id = GUID 783378b5-c9a0-49a9-8227-235f77509f55;
						}
						- m_pSender = { IHandle 
							- _m2Class = "IClassifierRole";
							- _id = GUID 783378b5-c9a0-49a9-8227-235f77509f55;
						}
						- m_pFormalMessage = { IHandle 
							- _m2Class = "";
						}
						- m_eType = CONDITION;
						- m_targetExec = { IHandle 
							- _m2Class = "";
						}
						- m_srcExec = { IHandle 
							- _m2Class = "";
						}
					}
					{ IMessage 
						- _id = GUID 0e6a7d2d-4de5-48e1-b426-cb181b871775;
						- _name = "Stop";
						- _modifiedTimeWeak = 1.1.1970::1:0:0;
						- m_szSequence = "6.";
						- m_szActualArgs = "";
						- m_szReturnVal = "";
						- m_pCommunicationConnection = { IHandle 
							- _m2Class = "";
						}
						- m_pReceiver = { IHandle 
							- _m2Class = "IClassifierRole";
							- _id = GUID b6b00713-6e03-4ec0-95ab-f01b5db15738;
						}
						- m_pSender = { IHandle 
							- _m2Class = "IClassifierRole";
							- _id = GUID d3a77353-9933-4ff7-b408-56cd6622e5ea;
						}
						- m_pFormalMessage = { IHandle 
							- _m2Class = "ITriggered";
							- _filename = "Default.sbs";
							- _subsystem = "Default";
							- _class = "HeightController";
							- _name = "Stop()";
							- _id = GUID 1d4a24bd-136e-47bf-a3c7-cd5e1684f9be;
						}
						- m_eType = TRIGGER;
						- m_targetExec = { IHandle 
							- _m2Class = "";
						}
						- m_srcExec = { IHandle 
							- _m2Class = "";
						}
					}
					{ IMessage 
						- _id = GUID 55613d73-5886-4dc9-aaf9-dd8a3c021c4a;
						- _properties = { IPropertyContainer 
							- Subjects = { IRPYRawContainer 
								- size = 1;
								- value = 
								{ IPropertySubject 
									- _Name = "SequenceDiagram";
									- Metaclasses = { IRPYRawContainer 
										- size = 1;
										- value = 
										{ IPropertyMetaclass 
											- _Name = "Condition_Mark";
											- Properties = { IRPYRawContainer 
												- size = 1;
												- value = 
												{ IProperty 
													- _Name = "IsStateCondition";
													- _Value = "True";
													- _Type = Bool;
												}
											}
										}
									}
								}
							}
						}
						- _name = "connector";
						- _modifiedTimeWeak = 1.1.1970::1:0:0;
						- m_szSequence = "";
						- m_szActualArgs = "";
						- m_szReturnVal = "";
						- m_freeText = "EmergencyStopped";
						- m_pCommunicationConnection = { IHandle 
							- _m2Class = "";
						}
						- m_pReceiver = { IHandle 
							- _m2Class = "IClassifierRole";
							- _id = GUID d3a77353-9933-4ff7-b408-56cd6622e5ea;
						}
						- m_pSender = { IHandle 
							- _m2Class = "IClassifierRole";
							- _id = GUID d3a77353-9933-4ff7-b408-56cd6622e5ea;
						}
						- m_pFormalMessage = { IHandle 
							- _m2Class = "";
						}
						- m_eType = CONDITION;
						- m_targetExec = { IHandle 
							- _m2Class = "";
						}
						- m_srcExec = { IHandle 
							- _m2Class = "";
						}
					}
					{ IMessage 
						- _id = GUID 55831158-806f-4ce6-9b71-8a2b43653b1d;
						- _properties = { IPropertyContainer 
							- Subjects = { IRPYRawContainer 
								- size = 1;
								- value = 
								{ IPropertySubject 
									- _Name = "SequenceDiagram";
									- Metaclasses = { IRPYRawContainer 
										- size = 1;
										- value = 
										{ IPropertyMetaclass 
											- _Name = "Condition_Mark";
											- Properties = { IRPYRawContainer 
												- size = 1;
												- value = 
												{ IProperty 
													- _Name = "IsStateCondition";
													- _Value = "True";
													- _Type = Bool;
												}
											}
										}
									}
								}
							}
						}
						- _name = "connector";
						- _modifiedTimeWeak = 1.1.1970::1:0:0;
						- m_szSequence = "";
						- m_szActualArgs = "";
						- m_szReturnVal = "";
						- m_freeText = "Init";
						- m_pCommunicationConnection = { IHandle 
							- _m2Class = "";
						}
						- m_pReceiver = { IHandle 
							- _m2Class = "IClassifierRole";
							- _id = GUID b6b00713-6e03-4ec0-95ab-f01b5db15738;
						}
						- m_pSender = { IHandle 
							- _m2Class = "IClassifierRole";
							- _id = GUID b6b00713-6e03-4ec0-95ab-f01b5db15738;
						}
						- m_pFormalMessage = { IHandle 
							- _m2Class = "";
						}
						- m_eType = CONDITION;
						- m_targetExec = { IHandle 
							- _m2Class = "";
						}
						- m_srcExec = { IHandle 
							- _m2Class = "";
						}
					}
					{ IMessage 
						- _id = GUID 50ace297-cb3d-471b-892c-6c08915f2cf7;
						- _myState = 8192;
						- _name = "tm";
						- _modifiedTimeWeak = 1.1.1970::1:0:0;
						- m_szSequence = "7.";
						- m_szActualArgs = "2000";
						- m_szReturnVal = "";
						- m_freeText = " at ROOT.state_5.accepteventaction_2";
						- m_pCommunicationConnection = { IHandle 
							- _m2Class = "";
						}
						- m_pReceiver = { IHandle 
							- _m2Class = "IClassifierRole";
							- _id = GUID 783378b5-c9a0-49a9-8227-235f77509f55;
						}
						- m_pSender = { IHandle 
							- _m2Class = "IClassifierRole";
							- _id = GUID 783378b5-c9a0-49a9-8227-235f77509f55;
						}
						- m_pFormalMessage = { IHandle 
							- _m2Class = "";
						}
						- m_eType = TIMEOUT;
						- m_targetExec = { IHandle 
							- _m2Class = "";
						}
						- m_srcExec = { IHandle 
							- _m2Class = "";
						}
					}
					{ IMessage 
						- _id = GUID ef02c74d-8c6e-418a-84b1-8e290617e1e8;
						- _name = "Up";
						- _modifiedTimeWeak = 1.1.1970::1:0:0;
						- m_szSequence = "8.";
						- m_szActualArgs = "";
						- m_szReturnVal = "";
						- m_pCommunicationConnection = { IHandle 
							- _m2Class = "";
						}
						- m_pReceiver = { IHandle 
							- _m2Class = "IClassifierRole";
							- _id = GUID b6b00713-6e03-4ec0-95ab-f01b5db15738;
						}
						- m_pSender = { IHandle 
							- _m2Class = "IClassifierRole";
							- _id = GUID 783378b5-c9a0-49a9-8227-235f77509f55;
						}
						- m_pFormalMessage = { IHandle 
							- _m2Class = "IEvent";
							- _filename = "Default.sbs";
							- _subsystem = "Default";
							- _class = "";
							- _name = "Up()";
							- _id = GUID e55ee974-7a59-4354-be2d-5918a481dadf;
						}
						- m_eType = EVENT;
						- m_targetExec = { IHandle 
							- _m2Class = "";
						}
						- m_srcExec = { IHandle 
							- _m2Class = "";
						}
					}
					{ IMessage 
						- _id = GUID 7b6ffd4f-c6e0-4d28-94c0-c773b97e433f;
						- _properties = { IPropertyContainer 
							- Subjects = { IRPYRawContainer 
								- size = 1;
								- value = 
								{ IPropertySubject 
									- _Name = "SequenceDiagram";
									- Metaclasses = { IRPYRawContainer 
										- size = 1;
										- value = 
										{ IPropertyMetaclass 
											- _Name = "Condition_Mark";
											- Properties = { IRPYRawContainer 
												- size = 1;
												- value = 
												{ IProperty 
													- _Name = "IsStateCondition";
													- _Value = "True";
													- _Type = Bool;
												}
											}
										}
									}
								}
							}
						}
						- _name = "connector";
						- _modifiedTimeWeak = 1.1.1970::1:0:0;
						- m_szSequence = "";
						- m_szActualArgs = "";
						- m_szReturnVal = "";
						- m_freeText = "NotWorking";
						- m_pCommunicationConnection = { IHandle 
							- _m2Class = "";
						}
						- m_pReceiver = { IHandle 
							- _m2Class = "IClassifierRole";
							- _id = GUID 783378b5-c9a0-49a9-8227-235f77509f55;
						}
						- m_pSender = { IHandle 
							- _m2Class = "IClassifierRole";
							- _id = GUID 783378b5-c9a0-49a9-8227-235f77509f55;
						}
						- m_pFormalMessage = { IHandle 
							- _m2Class = "";
						}
						- m_eType = CONDITION;
						- m_targetExec = { IHandle 
							- _m2Class = "";
						}
						- m_srcExec = { IHandle 
							- _m2Class = "";
						}
					}
					{ IMessage 
						- _id = GUID 56a76a34-5d92-4c69-9455-0a2f162ddc29;
						- _properties = { IPropertyContainer 
							- Subjects = { IRPYRawContainer 
								- size = 1;
								- value = 
								{ IPropertySubject 
									- _Name = "SequenceDiagram";
									- Metaclasses = { IRPYRawContainer 
										- size = 1;
										- value = 
										{ IPropertyMetaclass 
											- _Name = "Condition_Mark";
											- Properties = { IRPYRawContainer 
												- size = 1;
												- value = 
												{ IProperty 
													- _Name = "IsStateCondition";
													- _Value = "True";
													- _Type = Bool;
												}
											}
										}
									}
								}
							}
						}
						- _name = "connector";
						- _modifiedTimeWeak = 1.1.1970::1:0:0;
						- m_szSequence = "";
						- m_szActualArgs = "";
						- m_szReturnVal = "";
						- m_freeText = "EmergencyMoving";
						- m_pCommunicationConnection = { IHandle 
							- _m2Class = "";
						}
						- m_pReceiver = { IHandle 
							- _m2Class = "IClassifierRole";
							- _id = GUID d3a77353-9933-4ff7-b408-56cd6622e5ea;
						}
						- m_pSender = { IHandle 
							- _m2Class = "IClassifierRole";
							- _id = GUID d3a77353-9933-4ff7-b408-56cd6622e5ea;
						}
						- m_pFormalMessage = { IHandle 
							- _m2Class = "";
						}
						- m_eType = CONDITION;
						- m_targetExec = { IHandle 
							- _m2Class = "";
						}
						- m_srcExec = { IHandle 
							- _m2Class = "";
						}
					}
					{ IMessage 
						- _id = GUID 00059f90-b985-40b3-aab6-89da21e1696e;
						- _myState = 8192;
						- _name = "MoveControllerE";
						- _modifiedTimeWeak = 1.1.1970::1:0:0;
						- m_szSequence = "9.";
						- m_szActualArgs = "level = 0";
						- m_szReturnVal = "";
						- m_pCommunicationConnection = { IHandle 
							- _m2Class = "";
						}
						- m_pReceiver = { IHandle 
							- _m2Class = "IClassifierRole";
							- _id = GUID b6b00713-6e03-4ec0-95ab-f01b5db15738;
						}
						- m_pSender = { IHandle 
							- _m2Class = "IClassifierRole";
							- _id = GUID d3a77353-9933-4ff7-b408-56cd6622e5ea;
						}
						- m_pFormalMessage = { IHandle 
							- _m2Class = "IEvent";
							- _filename = "Default.sbs";
							- _subsystem = "Default";
							- _class = "";
							- _name = "MoveControllerE(int)";
							- _id = GUID 41513545-4957-4be8-9307-dcf62835f390;
						}
						- m_eType = EVENT;
						- m_targetExec = { IHandle 
							- _m2Class = "";
						}
						- m_srcExec = { IHandle 
							- _m2Class = "";
						}
					}
					{ IMessage 
						- _id = GUID 4c5a6f19-421c-446c-a78f-63f9161b94c3;
						- _properties = { IPropertyContainer 
							- Subjects = { IRPYRawContainer 
								- size = 1;
								- value = 
								{ IPropertySubject 
									- _Name = "SequenceDiagram";
									- Metaclasses = { IRPYRawContainer 
										- size = 1;
										- value = 
										{ IPropertyMetaclass 
											- _Name = "Condition_Mark";
											- Properties = { IRPYRawContainer 
												- size = 1;
												- value = 
												{ IProperty 
													- _Name = "IsStateCondition";
													- _Value = "True";
													- _Type = Bool;
												}
											}
										}
									}
								}
							}
						}
						- _name = "connector";
						- _modifiedTimeWeak = 1.1.1970::1:0:0;
						- m_szSequence = "";
						- m_szActualArgs = "";
						- m_szReturnVal = "";
						- m_freeText = "MovingDecision";
						- m_pCommunicationConnection = { IHandle 
							- _m2Class = "";
						}
						- m_pReceiver = { IHandle 
							- _m2Class = "IClassifierRole";
							- _id = GUID b6b00713-6e03-4ec0-95ab-f01b5db15738;
						}
						- m_pSender = { IHandle 
							- _m2Class = "IClassifierRole";
							- _id = GUID b6b00713-6e03-4ec0-95ab-f01b5db15738;
						}
						- m_pFormalMessage = { IHandle 
							- _m2Class = "";
						}
						- m_eType = CONDITION;
						- m_targetExec = { IHandle 
							- _m2Class = "";
						}
						- m_srcExec = { IHandle 
							- _m2Class = "";
						}
					}
					{ IMessage 
						- _id = GUID c5a5bd1e-6cf5-4753-ab5e-859f5dda51c6;
						- _name = "Down";
						- _modifiedTimeWeak = 1.1.1970::1:0:0;
						- m_szSequence = "10.";
						- m_szActualArgs = "";
						- m_szReturnVal = "";
						- m_pCommunicationConnection = { IHandle 
							- _m2Class = "";
						}
						- m_pReceiver = { IHandle 
							- _m2Class = "IClassifierRole";
							- _id = GUID 783378b5-c9a0-49a9-8227-235f77509f55;
						}
						- m_pSender = { IHandle 
							- _m2Class = "IClassifierRole";
							- _id = GUID b6b00713-6e03-4ec0-95ab-f01b5db15738;
						}
						- m_pFormalMessage = { IHandle 
							- _m2Class = "IEvent";
							- _filename = "Default.sbs";
							- _subsystem = "Default";
							- _class = "";
							- _name = "Down()";
							- _id = GUID ae879ce9-3f61-4ab5-b098-24ba6eaa8e93;
						}
						- m_eType = EVENT;
						- m_targetExec = { IHandle 
							- _m2Class = "";
						}
						- m_srcExec = { IHandle 
							- _m2Class = "";
						}
					}
					{ IMessage 
						- _id = GUID 66c3a03e-5ac4-4f29-a56f-ec716922737e;
						- _properties = { IPropertyContainer 
							- Subjects = { IRPYRawContainer 
								- size = 1;
								- value = 
								{ IPropertySubject 
									- _Name = "SequenceDiagram";
									- Metaclasses = { IRPYRawContainer 
										- size = 1;
										- value = 
										{ IPropertyMetaclass 
											- _Name = "Condition_Mark";
											- Properties = { IRPYRawContainer 
												- size = 1;
												- value = 
												{ IProperty 
													- _Name = "IsStateCondition";
													- _Value = "True";
													- _Type = Bool;
												}
											}
										}
									}
								}
							}
						}
						- _name = "connector";
						- _modifiedTimeWeak = 1.1.1970::1:0:0;
						- m_szSequence = "";
						- m_szActualArgs = "";
						- m_szReturnVal = "";
						- m_freeText = "BeforeWaitingForEvent";
						- m_pCommunicationConnection = { IHandle 
							- _m2Class = "";
						}
						- m_pReceiver = { IHandle 
							- _m2Class = "IClassifierRole";
							- _id = GUID b6b00713-6e03-4ec0-95ab-f01b5db15738;
						}
						- m_pSender = { IHandle 
							- _m2Class = "IClassifierRole";
							- _id = GUID b6b00713-6e03-4ec0-95ab-f01b5db15738;
						}
						- m_pFormalMessage = { IHandle 
							- _m2Class = "";
						}
						- m_eType = CONDITION;
						- m_targetExec = { IHandle 
							- _m2Class = "";
						}
						- m_srcExec = { IHandle 
							- _m2Class = "";
						}
					}
					{ IMessage 
						- _id = GUID 64297161-1352-4e56-9d4c-74dae44f31f5;
						- _properties = { IPropertyContainer 
							- Subjects = { IRPYRawContainer 
								- size = 1;
								- value = 
								{ IPropertySubject 
									- _Name = "SequenceDiagram";
									- Metaclasses = { IRPYRawContainer 
										- size = 1;
										- value = 
										{ IPropertyMetaclass 
											- _Name = "Condition_Mark";
											- Properties = { IRPYRawContainer 
												- size = 1;
												- value = 
												{ IProperty 
													- _Name = "IsStateCondition";
													- _Value = "True";
													- _Type = Bool;
												}
											}
										}
									}
								}
							}
						}
						- _name = "connector";
						- _modifiedTimeWeak = 1.1.1970::1:0:0;
						- m_szSequence = "";
						- m_szActualArgs = "";
						- m_szReturnVal = "";
						- m_freeText = "accepteventaction_1";
						- m_pCommunicationConnection = { IHandle 
							- _m2Class = "";
						}
						- m_pReceiver = { IHandle 
							- _m2Class = "IClassifierRole";
							- _id = GUID 783378b5-c9a0-49a9-8227-235f77509f55;
						}
						- m_pSender = { IHandle 
							- _m2Class = "IClassifierRole";
							- _id = GUID 783378b5-c9a0-49a9-8227-235f77509f55;
						}
						- m_pFormalMessage = { IHandle 
							- _m2Class = "";
						}
						- m_eType = CONDITION;
						- m_targetExec = { IHandle 
							- _m2Class = "";
						}
						- m_srcExec = { IHandle 
							- _m2Class = "";
						}
					}
					{ IMessage 
						- _id = GUID e44cf4e0-41c5-4a8a-8b3d-51db55d5e2a4;
						- _myState = 8192;
						- _name = "tm";
						- _modifiedTimeWeak = 1.1.1970::1:0:0;
						- m_szSequence = "11.";
						- m_szActualArgs = "2000";
						- m_szReturnVal = "";
						- m_freeText = " at ROOT.state_5.accepteventaction_1";
						- m_pCommunicationConnection = { IHandle 
							- _m2Class = "";
						}
						- m_pReceiver = { IHandle 
							- _m2Class = "IClassifierRole";
							- _id = GUID 783378b5-c9a0-49a9-8227-235f77509f55;
						}
						- m_pSender = { IHandle 
							- _m2Class = "IClassifierRole";
							- _id = GUID 783378b5-c9a0-49a9-8227-235f77509f55;
						}
						- m_pFormalMessage = { IHandle 
							- _m2Class = "";
						}
						- m_eType = TIMEOUT;
						- m_targetExec = { IHandle 
							- _m2Class = "";
						}
						- m_srcExec = { IHandle 
							- _m2Class = "";
						}
					}
					{ IMessage 
						- _id = GUID b093ee04-acd3-40cd-b867-d244b42ac21b;
						- _name = "Down";
						- _modifiedTimeWeak = 1.1.1970::1:0:0;
						- m_szSequence = "12.";
						- m_szActualArgs = "";
						- m_szReturnVal = "";
						- m_pCommunicationConnection = { IHandle 
							- _m2Class = "";
						}
						- m_pReceiver = { IHandle 
							- _m2Class = "IClassifierRole";
							- _id = GUID b6b00713-6e03-4ec0-95ab-f01b5db15738;
						}
						- m_pSender = { IHandle 
							- _m2Class = "IClassifierRole";
							- _id = GUID 783378b5-c9a0-49a9-8227-235f77509f55;
						}
						- m_pFormalMessage = { IHandle 
							- _m2Class = "IEvent";
							- _filename = "Default.sbs";
							- _subsystem = "Default";
							- _class = "";
							- _name = "Down()";
							- _id = GUID ae879ce9-3f61-4ab5-b098-24ba6eaa8e93;
						}
						- m_eType = EVENT;
						- m_targetExec = { IHandle 
							- _m2Class = "";
						}
						- m_srcExec = { IHandle 
							- _m2Class = "";
						}
					}
					{ IMessage 
						- _id = GUID 9e7f27ec-d7dc-4d8a-8305-07038b89d95f;
						- _properties = { IPropertyContainer 
							- Subjects = { IRPYRawContainer 
								- size = 1;
								- value = 
								{ IPropertySubject 
									- _Name = "SequenceDiagram";
									- Metaclasses = { IRPYRawContainer 
										- size = 1;
										- value = 
										{ IPropertyMetaclass 
											- _Name = "Condition_Mark";
											- Properties = { IRPYRawContainer 
												- size = 1;
												- value = 
												{ IProperty 
													- _Name = "IsStateCondition";
													- _Value = "True";
													- _Type = Bool;
												}
											}
										}
									}
								}
							}
						}
						- _name = "connector";
						- _modifiedTimeWeak = 1.1.1970::1:0:0;
						- m_szSequence = "";
						- m_szActualArgs = "";
						- m_szReturnVal = "";
						- m_freeText = "NotWorking";
						- m_pCommunicationConnection = { IHandle 
							- _m2Class = "";
						}
						- m_pReceiver = { IHandle 
							- _m2Class = "IClassifierRole";
							- _id = GUID 783378b5-c9a0-49a9-8227-235f77509f55;
						}
						- m_pSender = { IHandle 
							- _m2Class = "IClassifierRole";
							- _id = GUID 783378b5-c9a0-49a9-8227-235f77509f55;
						}
						- m_pFormalMessage = { IHandle 
							- _m2Class = "";
						}
						- m_eType = CONDITION;
						- m_targetExec = { IHandle 
							- _m2Class = "";
						}
						- m_srcExec = { IHandle 
							- _m2Class = "";
						}
					}
					{ IMessage 
						- _id = GUID 71db86f5-478c-4fe6-97a8-2d3c27a58d0e;
						- _properties = { IPropertyContainer 
							- Subjects = { IRPYRawContainer 
								- size = 1;
								- value = 
								{ IPropertySubject 
									- _Name = "SequenceDiagram";
									- Metaclasses = { IRPYRawContainer 
										- size = 1;
										- value = 
										{ IPropertyMetaclass 
											- _Name = "Condition_Mark";
											- Properties = { IRPYRawContainer 
												- size = 1;
												- value = 
												{ IProperty 
													- _Name = "IsStateCondition";
													- _Value = "True";
													- _Type = Bool;
												}
											}
										}
									}
								}
							}
						}
						- _name = "connector";
						- _modifiedTimeWeak = 1.1.1970::1:0:0;
						- m_szSequence = "";
						- m_szActualArgs = "";
						- m_szReturnVal = "";
						- m_freeText = "MovingDecision";
						- m_pCommunicationConnection = { IHandle 
							- _m2Class = "";
						}
						- m_pReceiver = { IHandle 
							- _m2Class = "IClassifierRole";
							- _id = GUID b6b00713-6e03-4ec0-95ab-f01b5db15738;
						}
						- m_pSender = { IHandle 
							- _m2Class = "IClassifierRole";
							- _id = GUID b6b00713-6e03-4ec0-95ab-f01b5db15738;
						}
						- m_pFormalMessage = { IHandle 
							- _m2Class = "";
						}
						- m_eType = CONDITION;
						- m_targetExec = { IHandle 
							- _m2Class = "";
						}
						- m_srcExec = { IHandle 
							- _m2Class = "";
						}
					}
					{ IMessage 
						- _id = GUID bb0c49f7-dfbc-4f42-af0b-1cee8b6725a2;
						- _properties = { IPropertyContainer 
							- Subjects = { IRPYRawContainer 
								- size = 1;
								- value = 
								{ IPropertySubject 
									- _Name = "SequenceDiagram";
									- Metaclasses = { IRPYRawContainer 
										- size = 1;
										- value = 
										{ IPropertyMetaclass 
											- _Name = "Condition_Mark";
											- Properties = { IRPYRawContainer 
												- size = 1;
												- value = 
												{ IProperty 
													- _Name = "IsStateCondition";
													- _Value = "True";
													- _Type = Bool;
												}
											}
										}
									}
								}
							}
						}
						- _name = "connector";
						- _modifiedTimeWeak = 1.1.1970::1:0:0;
						- m_szSequence = "";
						- m_szActualArgs = "";
						- m_szReturnVal = "";
						- m_freeText = "SendEvent";
						- m_pCommunicationConnection = { IHandle 
							- _m2Class = "";
						}
						- m_pReceiver = { IHandle 
							- _m2Class = "IClassifierRole";
							- _id = GUID b6b00713-6e03-4ec0-95ab-f01b5db15738;
						}
						- m_pSender = { IHandle 
							- _m2Class = "IClassifierRole";
							- _id = GUID b6b00713-6e03-4ec0-95ab-f01b5db15738;
						}
						- m_pFormalMessage = { IHandle 
							- _m2Class = "";
						}
						- m_eType = CONDITION;
						- m_targetExec = { IHandle 
							- _m2Class = "";
						}
						- m_srcExec = { IHandle 
							- _m2Class = "";
						}
					}
					{ IMessage 
						- _id = GUID 13b2f242-51fa-4c28-bc55-72d90833accf;
						- _name = "LevelController";
						- _modifiedTimeWeak = 1.1.1970::1:0:0;
						- m_szSequence = "13.";
						- m_szActualArgs = "";
						- m_szReturnVal = "";
						- m_pCommunicationConnection = { IHandle 
							- _m2Class = "";
						}
						- m_pReceiver = { IHandle 
							- _m2Class = "IClassifierRole";
							- _id = GUID d3a77353-9933-4ff7-b408-56cd6622e5ea;
						}
						- m_pSender = { IHandle 
							- _m2Class = "IClassifierRole";
							- _id = GUID b6b00713-6e03-4ec0-95ab-f01b5db15738;
						}
						- m_pFormalMessage = { IHandle 
							- _m2Class = "IEvent";
							- _filename = "Default.sbs";
							- _subsystem = "Default";
							- _class = "";
							- _name = "LevelController()";
							- _id = GUID 601e302e-c3c8-46b7-aa4e-75a45337f13a;
						}
						- m_eType = EVENT;
						- m_targetExec = { IHandle 
							- _m2Class = "";
						}
						- m_srcExec = { IHandle 
							- _m2Class = "";
						}
					}
					{ IMessage 
						- _id = GUID b32f9644-ff59-4b7e-a40d-d9a9566122b3;
						- _properties = { IPropertyContainer 
							- Subjects = { IRPYRawContainer 
								- size = 1;
								- value = 
								{ IPropertySubject 
									- _Name = "SequenceDiagram";
									- Metaclasses = { IRPYRawContainer 
										- size = 1;
										- value = 
										{ IPropertyMetaclass 
											- _Name = "Condition_Mark";
											- Properties = { IRPYRawContainer 
												- size = 1;
												- value = 
												{ IProperty 
													- _Name = "IsStateCondition";
													- _Value = "True";
													- _Type = Bool;
												}
											}
										}
									}
								}
							}
						}
						- _name = "connector";
						- _modifiedTimeWeak = 1.1.1970::1:0:0;
						- m_szSequence = "";
						- m_szActualArgs = "";
						- m_szReturnVal = "";
						- m_freeText = "EmergencyBaseLevel";
						- m_pCommunicationConnection = { IHandle 
							- _m2Class = "";
						}
						- m_pReceiver = { IHandle 
							- _m2Class = "IClassifierRole";
							- _id = GUID d3a77353-9933-4ff7-b408-56cd6622e5ea;
						}
						- m_pSender = { IHandle 
							- _m2Class = "IClassifierRole";
							- _id = GUID d3a77353-9933-4ff7-b408-56cd6622e5ea;
						}
						- m_pFormalMessage = { IHandle 
							- _m2Class = "";
						}
						- m_eType = CONDITION;
						- m_targetExec = { IHandle 
							- _m2Class = "";
						}
						- m_srcExec = { IHandle 
							- _m2Class = "";
						}
					}
				}
			}
		}
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

