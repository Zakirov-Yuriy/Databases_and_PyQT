<?xml version="1.0" encoding="UTF-8"?>
<ui version="4.0">
 <class>MainWindow</class>
 <widget class="QMainWindow" name="MainWindow">
  <property name="geometry">
   <rect>
    <x>0</x>
    <y>0</y>
    <width>620</width>
    <height>531</height>
   </rect>
  </property>
  <property name="windowTitle">
   <string>MainWindow</string>
  </property>
  <property name="styleSheet">
   <string notr="true">background-color: rgb(170, 255, 127);
background-color: rgb(255, 255, 255);</string>
  </property>
  <widget class="QWidget" name="centralwidget">
   <layout class="QVBoxLayout" name="verticalLayout">
    <property name="sizeConstraint">
     <enum>QLayout::SetMinAndMaxSize</enum>
    </property>
    <item>
     <layout class="QGridLayout" name="gridLayout_web">
      <property name="sizeConstraint">
       <enum>QLayout::SetMinAndMaxSize</enum>
      </property>
      <item row="0" column="0">
       <widget class="QTabWidget" name="tabWidget">
        <property name="minimumSize">
         <size>
          <width>600</width>
          <height>0</height>
         </size>
        </property>
        <property name="currentIndex">
         <number>1</number>
        </property>
        <widget class="QWidget" name="tabUser">
         <property name="maximumSize">
          <size>
           <width>596</width>
           <height>484</height>
          </size>
         </property>
         <attribute name="title">
          <string>Список контактов</string>
         </attribute>
         <layout class="QVBoxLayout" name="verticalLayout_2">
          <item>
           <widget class="QPushButton" name="pushButton">
            <property name="text">
             <string>Обновить список</string>
            </property>
            <property name="checkable">
             <bool>false</bool>
            </property>
           </widget>
          </item>
          <item>
           <widget class="QTableView" name="tableViewUser"/>
          </item>
         </layout>
        </widget>
        <widget class="QWidget" name="tabSettings">
         <attribute name="title">
          <string>Настройки</string>
         </attribute>
         <widget class="QPushButton" name="pushButtonConnect">
          <property name="geometry">
           <rect>
            <x>10</x>
            <y>10</y>
            <width>82</width>
            <height>22</height>
           </rect>
          </property>
          <property name="text">
           <string>Подключиться</string>
          </property>
         </widget>
         <widget class="QLineEdit" name="lineEdit">
          <property name="geometry">
           <rect>
            <x>40</x>
            <y>50</y>
            <width>91</width>
            <height>22</height>
           </rect>
          </property>
         </widget>
         <widget class="QLabel" name="labelPort">
          <property name="enabled">
           <bool>true</bool>
          </property>
          <property name="geometry">
           <rect>
            <x>10</x>
            <y>50</y>
            <width>33</width>
            <height>20</height>
           </rect>
          </property>
          <property name="maximumSize">
           <size>
            <width>33</width>
            <height>20</height>
           </size>
          </property>
          <property name="text">
           <string>Порт</string>
          </property>
         </widget>
        </widget>
       </widget>
      </item>
     </layout>
    </item>
   </layout>
  </widget>
  <action name="open">
   <property name="text">
    <string>Открыть бд</string>
   </property>
  </action>
  <action name="actionadd_row">
   <property name="text">
    <string>add_row</string>
   </property>
  </action>
  <action name="actiondel_row">
   <property name="text">
    <string>del_row</string>
   </property>
  </action>
  <action name="actionsave">
   <property name="text">
    <string>save</string>
   </property>
  </action>
 </widget>
 <resources/>
 <connections/>
</ui>