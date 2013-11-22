I-Logix-RPY-Archive version 8.8.0 Java 6107223
{ IProject 
	- _id = GUID 0c8283b7-8ceb-4ff1-b6c8-24b29e07e251;
	- _myState = 8192;
	- _name = "Elevator";
	- _modifiedTimeWeak = 11.22.2013::11:23:21;
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
		- _filename = "exe.cmp";
		- _subsystem = "";
		- _class = "";
		- _name = "exe";
		- _id = GUID d90e55dd-0cab-4770-8e09-c67348fe3912;
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
		- size = 1;
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

