<?xml version="1.0" encoding="UTF-8"?>
<ui version="4.0">
 <class>MainClientWindow</class>
 <widget class="QMainWindow" name="MainClientWindow">
  <property name="geometry">
   <rect>
    <x>0</x>
    <y>0</y>
    <width>756</width>
    <height>534</height>
   </rect>
  </property>
  <property name="minimumSize">
   <size>
    <width>756</width>
    <height>534</height>
   </size>
  </property>
  <property name="windowTitle">
   <string>Чат Программа</string>
  </property>
  <widget class="QWidget" name="centralwidget">
   <widget class="QLabel" name="label_contacts">
    <property name="geometry">
     <rect>
      <x>10</x>
      <y>0</y>
      <width>101</width>
      <height>16</height>
     </rect>
    </property>
    <property name="text">
     <string>Список контактов:</string>
    </property>
   </widget>
   <widget class="QLabel" name="label_history">
    <property name="geometry">
     <rect>
      <x>300</x>
      <y>0</y>
      <width>391</width>
      <height>21</height>
     </rect>
    </property>
    <property name="text">
     <string>История сообщений:</string>
    </property>
   </widget>
   <widget class="QTextEdit" name="text_message">
    <property name="geometry">
     <rect>
      <x>300</x>
      <y>360</y>
      <width>441</width>
      <height>71</height>
     </rect>
    </property>
   </widget>
   <widget class="QLabel" name="label_new_message">
    <property name="geometry">
     <rect>
      <x>300</x>
      <y>330</y>
      <width>171</width>
      <height>16</height>
     </rect>
    </property>
    <property name="text">
     <string>Введите новое сообщение:</string>
    </property>
   </widget>
   <widget class="QListView" name="list_contacts">
    <property name="geometry">
     <rect>
      <x>10</x>
      <y>20</y>
      <width>271</width>
      <height>411</height>
     </rect>
    </property>
   </widget>
   <widget class="QListView" name="list_messages">
    <property name="geometry">
     <rect>
      <x>300</x>
      <y>20</y>
      <width>441</width>
      <height>301</height>
     </rect>
    </property>
   </widget>
   <widget class="QPushButton" name="btn_send">
    <property name="geometry">
     <rect>
      <x>610</x>
      <y>450</y>
      <width>131</width>
      <height>31</height>
     </rect>
    </property>
    <property name="text">
     <string>Отправить сообщение</string>
    </property>
   </widget>
   <widget class="QPushButton" name="btn_clear">
    <property name="geometry">
     <rect>
      <x>460</x>
      <y>450</y>
      <width>131</width>
      <height>31</height>
     </rect>
    </property>
    <property name="text">
     <string>Очистить поле</string>
    </property>
   </widget>
   <widget class="QPushButton" name="btn_get_list">
    <property name="geometry">
     <rect>
      <x>10</x>
      <y>450</y>
      <width>161</width>
      <height>31</height>
     </rect>
    </property>
    <property name="text">
     <string>Обновить список контактов</string>
    </property>
   </widget>
   <widget class="QPushButton" name="btn_add_contact">
    <property name="geometry">
     <rect>
      <x>180</x>
      <y>450</y>
      <width>101</width>
      <height>31</height>
     </rect>
    </property>
    <property name="text">
     <string>Добавить контакт</string>
    </property>
   </widget>
  </widget>
  <widget class="QStatusBar" name="statusBar"/>
  <action name="menu_exit">
   <property name="text">
    <string>Выход</string>
   </property>
  </action>
  <action name="menu_add_contact">
   <property name="text">
    <string>Добавить контакт</string>
   </property>
  </action>
  <action name="menu_del_contact">
   <property name="text">
    <string>Удалить контакт</string>
   </property>
  </action>
 </widget>
 <resources/>
 <connections>
  <connection>
   <sender>btn_clear</sender>
   <signal>clicked()</signal>
   <receiver>text_message</receiver>
   <slot>clear()</slot>
   <hints>
    <hint type="sourcelabel">
     <x>541</x>
     <y>481</y>
    </hint>
    <hint type="destinationlabel">
     <x>547</x>
     <y>416</y>
    </hint>
   </hints>
  </connection>
 </connections>
</ui>