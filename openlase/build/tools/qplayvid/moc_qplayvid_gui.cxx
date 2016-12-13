/****************************************************************************
** Meta object code from reading C++ file 'qplayvid_gui.h'
**
** Created by: The Qt Meta Object Compiler version 63 (Qt 4.8.7)
**
** WARNING! All changes made in this file will be lost!
*****************************************************************************/

#include "../../../tools/qplayvid/qplayvid_gui.h"
#if !defined(Q_MOC_OUTPUT_REVISION)
#error "The header file 'qplayvid_gui.h' doesn't include <QObject>."
#elif Q_MOC_OUTPUT_REVISION != 63
#error "This file was generated using the moc from 4.8.7. It"
#error "cannot be used with the include files from this version of Qt."
#error "(The moc has changed too much.)"
#endif

QT_BEGIN_MOC_NAMESPACE
static const uint qt_meta_data_PlayerSetting[] = {

 // content:
       6,       // revision
       0,       // classname
       0,    0, // classinfo
       3,   14, // methods
       0,    0, // properties
       0,    0, // enums/sets
       0,    0, // constructors
       0,       // flags
       1,       // signalCount

 // signals: signature, parameters, type, tag, flags
      24,   15,   14,   14, 0x05,

 // slots: signature, parameters, type, tag, flags
      48,   42,   14,   14, 0x0a,
      70,   62,   14,   14, 0x0a,

       0        // eod
};

static const char qt_meta_stringdata_PlayerSetting[] = {
    "PlayerSetting\0\0newValue\0valueChanged(int)\0"
    "value\0setValue(int)\0enabled\0"
    "setEnabled(bool)\0"
};

void PlayerSetting::qt_static_metacall(QObject *_o, QMetaObject::Call _c, int _id, void **_a)
{
    if (_c == QMetaObject::InvokeMetaMethod) {
        Q_ASSERT(staticMetaObject.cast(_o));
        PlayerSetting *_t = static_cast<PlayerSetting *>(_o);
        switch (_id) {
        case 0: _t->valueChanged((*reinterpret_cast< int(*)>(_a[1]))); break;
        case 1: _t->setValue((*reinterpret_cast< int(*)>(_a[1]))); break;
        case 2: _t->setEnabled((*reinterpret_cast< bool(*)>(_a[1]))); break;
        default: ;
        }
    }
}

const QMetaObjectExtraData PlayerSetting::staticMetaObjectExtraData = {
    0,  qt_static_metacall 
};

const QMetaObject PlayerSetting::staticMetaObject = {
    { &QObject::staticMetaObject, qt_meta_stringdata_PlayerSetting,
      qt_meta_data_PlayerSetting, &staticMetaObjectExtraData }
};

#ifdef Q_NO_DATA_RELOCATION
const QMetaObject &PlayerSetting::getStaticMetaObject() { return staticMetaObject; }
#endif //Q_NO_DATA_RELOCATION

const QMetaObject *PlayerSetting::metaObject() const
{
    return QObject::d_ptr->metaObject ? QObject::d_ptr->metaObject : &staticMetaObject;
}

void *PlayerSetting::qt_metacast(const char *_clname)
{
    if (!_clname) return 0;
    if (!strcmp(_clname, qt_meta_stringdata_PlayerSetting))
        return static_cast<void*>(const_cast< PlayerSetting*>(this));
    return QObject::qt_metacast(_clname);
}

int PlayerSetting::qt_metacall(QMetaObject::Call _c, int _id, void **_a)
{
    _id = QObject::qt_metacall(_c, _id, _a);
    if (_id < 0)
        return _id;
    if (_c == QMetaObject::InvokeMetaMethod) {
        if (_id < 3)
            qt_static_metacall(this, _c, _id, _a);
        _id -= 3;
    }
    return _id;
}

// SIGNAL 0
void PlayerSetting::valueChanged(int _t1)
{
    void *_a[] = { 0, const_cast<void*>(reinterpret_cast<const void*>(&_t1)) };
    QMetaObject::activate(this, &staticMetaObject, 0, _a);
}
static const uint qt_meta_data_PlayerUI[] = {

 // content:
       6,       // revision
       0,       // classname
       0,    0, // classinfo
      12,   14, // methods
       0,    0, // properties
       0,    0, // enums/sets
       0,    0, // constructors
       0,       // flags
       0,       // signalCount

 // slots: signature, parameters, type, tag, flags
      10,    9,    9,    9, 0x08,
      24,    9,    9,    9, 0x08,
      39,    9,    9,    9, 0x08,
      56,    9,    9,    9, 0x08,
      75,    9,    9,    9, 0x08,
      99,   93,    9,    9, 0x08,
     118,    9,    9,    9, 0x08,
     132,    9,    9,    9, 0x08,
     146,    9,    9,    9, 0x08,
     167,  161,    9,    9, 0x08,
     182,    9,    9,    9, 0x08,
     197,    9,    9,    9, 0x08,

       0        // eod
};

static const char qt_meta_stringdata_PlayerUI[] = {
    "PlayerUI\0\0modeChanged()\0splitChanged()\0"
    "updateSettings()\0updateSettingsUI()\0"
    "playStopClicked()\0pause\0pauseToggled(bool)\0"
    "stepClicked()\0timePressed()\0timeReleased()\0"
    "value\0timeMoved(int)\0loadSettings()\0"
    "saveSettings()\0"
};

void PlayerUI::qt_static_metacall(QObject *_o, QMetaObject::Call _c, int _id, void **_a)
{
    if (_c == QMetaObject::InvokeMetaMethod) {
        Q_ASSERT(staticMetaObject.cast(_o));
        PlayerUI *_t = static_cast<PlayerUI *>(_o);
        switch (_id) {
        case 0: _t->modeChanged(); break;
        case 1: _t->splitChanged(); break;
        case 2: _t->updateSettings(); break;
        case 3: _t->updateSettingsUI(); break;
        case 4: _t->playStopClicked(); break;
        case 5: _t->pauseToggled((*reinterpret_cast< bool(*)>(_a[1]))); break;
        case 6: _t->stepClicked(); break;
        case 7: _t->timePressed(); break;
        case 8: _t->timeReleased(); break;
        case 9: _t->timeMoved((*reinterpret_cast< int(*)>(_a[1]))); break;
        case 10: _t->loadSettings(); break;
        case 11: _t->saveSettings(); break;
        default: ;
        }
    }
}

const QMetaObjectExtraData PlayerUI::staticMetaObjectExtraData = {
    0,  qt_static_metacall 
};

const QMetaObject PlayerUI::staticMetaObject = {
    { &QMainWindow::staticMetaObject, qt_meta_stringdata_PlayerUI,
      qt_meta_data_PlayerUI, &staticMetaObjectExtraData }
};

#ifdef Q_NO_DATA_RELOCATION
const QMetaObject &PlayerUI::getStaticMetaObject() { return staticMetaObject; }
#endif //Q_NO_DATA_RELOCATION

const QMetaObject *PlayerUI::metaObject() const
{
    return QObject::d_ptr->metaObject ? QObject::d_ptr->metaObject : &staticMetaObject;
}

void *PlayerUI::qt_metacast(const char *_clname)
{
    if (!_clname) return 0;
    if (!strcmp(_clname, qt_meta_stringdata_PlayerUI))
        return static_cast<void*>(const_cast< PlayerUI*>(this));
    return QMainWindow::qt_metacast(_clname);
}

int PlayerUI::qt_metacall(QMetaObject::Call _c, int _id, void **_a)
{
    _id = QMainWindow::qt_metacall(_c, _id, _a);
    if (_id < 0)
        return _id;
    if (_c == QMetaObject::InvokeMetaMethod) {
        if (_id < 12)
            qt_static_metacall(this, _c, _id, _a);
        _id -= 12;
    }
    return _id;
}
QT_END_MOC_NAMESPACE
