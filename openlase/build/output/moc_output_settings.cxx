/****************************************************************************
** Meta object code from reading C++ file 'output_settings.h'
**
** Created by: The Qt Meta Object Compiler version 63 (Qt 4.8.7)
**
** WARNING! All changes made in this file will be lost!
*****************************************************************************/

#include "../../output/output_settings.h"
#if !defined(Q_MOC_OUTPUT_REVISION)
#error "The header file 'output_settings.h' doesn't include <QObject>."
#elif Q_MOC_OUTPUT_REVISION != 63
#error "This file was generated using the moc from 4.8.7. It"
#error "cannot be used with the include files from this version of Qt."
#error "(The moc has changed too much.)"
#endif

QT_BEGIN_MOC_NAMESPACE
static const uint qt_meta_data_OutputSettings[] = {

 // content:
       6,       // revision
       0,       // classname
       0,    0, // classinfo
      37,   14, // methods
       0,    0, // properties
       0,    0, // enums/sets
       0,    0, // constructors
       0,       // flags
       0,       // signalCount

 // slots: signature, parameters, type, tag, flags
      22,   16,   15,   15, 0x0a,
      52,   16,   15,   15, 0x0a,
      84,   16,   15,   15, 0x0a,
     122,  116,   15,   15, 0x0a,
     160,  116,   15,   15, 0x0a,
     202,   16,   15,   15, 0x0a,
     227,   16,   15,   15, 0x0a,
     252,   16,   15,   15, 0x0a,
     277,   16,   15,   15, 0x0a,
     302,   16,   15,   15, 0x0a,
     326,  116,   15,   15, 0x0a,
     366,   16,   15,   15, 0x0a,
     395,   16,   15,   15, 0x0a,
     422,   16,   15,   15, 0x0a,
     453,   15,   15,   15, 0x0a,
     477,   15,   15,   15, 0x0a,
     502,   16,   15,   15, 0x0a,
     535,  529,   15,   15, 0x0a,
     566,  529,   15,   15, 0x0a,
     597,  529,   15,   15, 0x0a,
     630,  529,   15,   15, 0x0a,
     663,   16,   15,   15, 0x0a,
     692,  529,   15,   15, 0x0a,
     725,  529,   15,   15, 0x0a,
     758,  529,   15,   15, 0x0a,
     793,  529,   15,   15, 0x0a,
     828,   16,   15,   15, 0x0a,
     856,  529,   15,   15, 0x0a,
     888,  529,   15,   15, 0x0a,
     920,  529,   15,   15, 0x0a,
     954,  529,   15,   15, 0x0a,
     988,  529,   15,   15, 0x0a,
    1018,  529,   15,   15, 0x0a,
    1047,   15,   15,   15, 0x0a,
    1081, 1075,   15,   15, 0x0a,
    1108, 1075,   15,   15, 0x0a,
    1134, 1131,   15,   15, 0x0a,

       0        // eod
};

static const char qt_meta_stringdata_OutputSettings[] = {
    "OutputSettings\0\0state\0"
    "on_outputEnable_toggled(bool)\0"
    "on_blankingEnable_toggled(bool)\0"
    "on_blankingInvert_toggled(bool)\0index\0"
    "on_colorMode_currentIndexChanged(int)\0"
    "on_colorChannels_currentIndexChanged(int)\0"
    "on_xEnable_toggled(bool)\0"
    "on_yEnable_toggled(bool)\0"
    "on_xInvert_toggled(bool)\0"
    "on_yInvert_toggled(bool)\0"
    "on_xySwap_toggled(bool)\0"
    "on_aspectRatio_currentIndexChanged(int)\0"
    "on_aspectScale_toggled(bool)\0"
    "on_fitSquare_toggled(bool)\0"
    "on_enforceSafety_toggled(bool)\0"
    "on_outputTest_pressed()\0"
    "on_outputTest_released()\0"
    "on_redEnable_toggled(bool)\0value\0"
    "on_redMaxBox_valueChanged(int)\0"
    "on_redMinBox_valueChanged(int)\0"
    "on_redBlankBox_valueChanged(int)\0"
    "on_redDelayBox_valueChanged(int)\0"
    "on_greenEnable_toggled(bool)\0"
    "on_greenMaxBox_valueChanged(int)\0"
    "on_greenMinBox_valueChanged(int)\0"
    "on_greenBlankBox_valueChanged(int)\0"
    "on_greenDelayBox_valueChanged(int)\0"
    "on_blueEnable_toggled(bool)\0"
    "on_blueMaxBox_valueChanged(int)\0"
    "on_blueMinBox_valueChanged(int)\0"
    "on_blueBlankBox_valueChanged(int)\0"
    "on_blueDelayBox_valueChanged(int)\0"
    "on_powerBox_valueChanged(int)\0"
    "on_sizeBox_valueChanged(int)\0"
    "on_resetTransform_clicked()\0event\0"
    "resizeEvent(QResizeEvent*)\0"
    "showEvent(QShowEvent*)\0pt\0"
    "pointMoved(ControlPoint*)\0"
};

void OutputSettings::qt_static_metacall(QObject *_o, QMetaObject::Call _c, int _id, void **_a)
{
    if (_c == QMetaObject::InvokeMetaMethod) {
        Q_ASSERT(staticMetaObject.cast(_o));
        OutputSettings *_t = static_cast<OutputSettings *>(_o);
        switch (_id) {
        case 0: _t->on_outputEnable_toggled((*reinterpret_cast< bool(*)>(_a[1]))); break;
        case 1: _t->on_blankingEnable_toggled((*reinterpret_cast< bool(*)>(_a[1]))); break;
        case 2: _t->on_blankingInvert_toggled((*reinterpret_cast< bool(*)>(_a[1]))); break;
        case 3: _t->on_colorMode_currentIndexChanged((*reinterpret_cast< int(*)>(_a[1]))); break;
        case 4: _t->on_colorChannels_currentIndexChanged((*reinterpret_cast< int(*)>(_a[1]))); break;
        case 5: _t->on_xEnable_toggled((*reinterpret_cast< bool(*)>(_a[1]))); break;
        case 6: _t->on_yEnable_toggled((*reinterpret_cast< bool(*)>(_a[1]))); break;
        case 7: _t->on_xInvert_toggled((*reinterpret_cast< bool(*)>(_a[1]))); break;
        case 8: _t->on_yInvert_toggled((*reinterpret_cast< bool(*)>(_a[1]))); break;
        case 9: _t->on_xySwap_toggled((*reinterpret_cast< bool(*)>(_a[1]))); break;
        case 10: _t->on_aspectRatio_currentIndexChanged((*reinterpret_cast< int(*)>(_a[1]))); break;
        case 11: _t->on_aspectScale_toggled((*reinterpret_cast< bool(*)>(_a[1]))); break;
        case 12: _t->on_fitSquare_toggled((*reinterpret_cast< bool(*)>(_a[1]))); break;
        case 13: _t->on_enforceSafety_toggled((*reinterpret_cast< bool(*)>(_a[1]))); break;
        case 14: _t->on_outputTest_pressed(); break;
        case 15: _t->on_outputTest_released(); break;
        case 16: _t->on_redEnable_toggled((*reinterpret_cast< bool(*)>(_a[1]))); break;
        case 17: _t->on_redMaxBox_valueChanged((*reinterpret_cast< int(*)>(_a[1]))); break;
        case 18: _t->on_redMinBox_valueChanged((*reinterpret_cast< int(*)>(_a[1]))); break;
        case 19: _t->on_redBlankBox_valueChanged((*reinterpret_cast< int(*)>(_a[1]))); break;
        case 20: _t->on_redDelayBox_valueChanged((*reinterpret_cast< int(*)>(_a[1]))); break;
        case 21: _t->on_greenEnable_toggled((*reinterpret_cast< bool(*)>(_a[1]))); break;
        case 22: _t->on_greenMaxBox_valueChanged((*reinterpret_cast< int(*)>(_a[1]))); break;
        case 23: _t->on_greenMinBox_valueChanged((*reinterpret_cast< int(*)>(_a[1]))); break;
        case 24: _t->on_greenBlankBox_valueChanged((*reinterpret_cast< int(*)>(_a[1]))); break;
        case 25: _t->on_greenDelayBox_valueChanged((*reinterpret_cast< int(*)>(_a[1]))); break;
        case 26: _t->on_blueEnable_toggled((*reinterpret_cast< bool(*)>(_a[1]))); break;
        case 27: _t->on_blueMaxBox_valueChanged((*reinterpret_cast< int(*)>(_a[1]))); break;
        case 28: _t->on_blueMinBox_valueChanged((*reinterpret_cast< int(*)>(_a[1]))); break;
        case 29: _t->on_blueBlankBox_valueChanged((*reinterpret_cast< int(*)>(_a[1]))); break;
        case 30: _t->on_blueDelayBox_valueChanged((*reinterpret_cast< int(*)>(_a[1]))); break;
        case 31: _t->on_powerBox_valueChanged((*reinterpret_cast< int(*)>(_a[1]))); break;
        case 32: _t->on_sizeBox_valueChanged((*reinterpret_cast< int(*)>(_a[1]))); break;
        case 33: _t->on_resetTransform_clicked(); break;
        case 34: _t->resizeEvent((*reinterpret_cast< QResizeEvent*(*)>(_a[1]))); break;
        case 35: _t->showEvent((*reinterpret_cast< QShowEvent*(*)>(_a[1]))); break;
        case 36: _t->pointMoved((*reinterpret_cast< ControlPoint*(*)>(_a[1]))); break;
        default: ;
        }
    }
}

const QMetaObjectExtraData OutputSettings::staticMetaObjectExtraData = {
    0,  qt_static_metacall 
};

const QMetaObject OutputSettings::staticMetaObject = {
    { &QMainWindow::staticMetaObject, qt_meta_stringdata_OutputSettings,
      qt_meta_data_OutputSettings, &staticMetaObjectExtraData }
};

#ifdef Q_NO_DATA_RELOCATION
const QMetaObject &OutputSettings::getStaticMetaObject() { return staticMetaObject; }
#endif //Q_NO_DATA_RELOCATION

const QMetaObject *OutputSettings::metaObject() const
{
    return QObject::d_ptr->metaObject ? QObject::d_ptr->metaObject : &staticMetaObject;
}

void *OutputSettings::qt_metacast(const char *_clname)
{
    if (!_clname) return 0;
    if (!strcmp(_clname, qt_meta_stringdata_OutputSettings))
        return static_cast<void*>(const_cast< OutputSettings*>(this));
    return QMainWindow::qt_metacast(_clname);
}

int OutputSettings::qt_metacall(QMetaObject::Call _c, int _id, void **_a)
{
    _id = QMainWindow::qt_metacall(_c, _id, _a);
    if (_id < 0)
        return _id;
    if (_c == QMetaObject::InvokeMetaMethod) {
        if (_id < 37)
            qt_static_metacall(this, _c, _id, _a);
        _id -= 37;
    }
    return _id;
}
QT_END_MOC_NAMESPACE
