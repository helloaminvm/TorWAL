windowmanager.cpp:563:48: error: invalid initialization of reference of type 'const WId&' {aka 'const long long unsigned int&'} from expression of type 'QString'
  563 |     for (const WId &key : existingWindows.keys()) {
      |                                                ^
windowmanager.cpp:564:32: error: invalid user-defined conversion from 'const WId' {aka 'const long long unsigned int'} to 'const QString&' [-fpermissive]
  564 |         if (!windowStillExists(key)) {
      |                                ^~~
In file included from ../../../../linuxbrew/.linuxbrew/Cellar/qt@5/5.15.13_1/include/QtCore/qobject.h:47,
                 from ../../../../linuxbrew/.linuxbrew/Cellar/qt@5/5.15.13_1/include/QtCore/qiodevice.h:45,
                 from ../../../../linuxbrew/.linuxbrew/Cellar/qt@5/5.15.13_1/include/QtCore/qtextstream.h:43:
../../../../linuxbrew/.linuxbrew/Cellar/qt@5/5.15.13_1/include/QtCore/qstring.h:832:31: note: candidate is: 'QString::QString(const char*)' (near match)
  832 |     inline QT_ASCII_CAST_WARN QString(const char *ch)
      |                               ^~~~~~~
../../../../linuxbrew/.linuxbrew/Cellar/qt@5/5.15.13_1/include/QtCore/qstring.h:832:31: note:   conversion of argument 1 would be ill-formed:
windowmanager.cpp:564:32: error: invalid conversion from 'WId' {aka 'long long unsigned int'} to 'const char*' [-fpermissive]
  564 |         if (!windowStillExists(key)) {
      |                                ^~~
      |                                |
      |                                WId {aka long long unsigned int}
windowmanager.cpp:564:32: error: invalid conversion from 'WId' {aka 'long long unsigned int'} to 'const char*' [-fpermissive]
  564 |         if (!windowStillExists(key)) {
      |                                ^~~
      |                                |
      |                                WId {aka long long unsigned int}
../../../../linuxbrew/.linuxbrew/Cellar/qt@5/5.15.13_1/include/QtCore/qstring.h:832:51: note:   initializing argument 1 of 'QString::QString(const char*)'
  832 |     inline QT_ASCII_CAST_WARN QString(const char *ch)
      |                                       ~~~~~~~~~~~~^~
windowmanager.cpp:75:54: note:   initializing argument 1 of 'bool WindowManager::windowStillExists(const QString&) const'
   75 | bool WindowManager::windowStillExists(const QString &name) const {
      |                                       ~~~~~~~~~~~~~~~^~~~
windowmanager.cpp:570:32: error: invalid user-defined conversion from 'const WId' {aka 'const long long unsigned int'} to 'const QString&' [-fpermissive]
  570 |         existingWindows.remove(key);
      |                                ^~~
../../../../linuxbrew/.linuxbrew/Cellar/qt@5/5.15.13_1/include/QtCore/qstring.h:832:31: note: candidate is: 'QString::QString(const char*)' (near match)
  832 |     inline QT_ASCII_CAST_WARN QString(const char *ch)
      |                               ^~~~~~~
../../../../linuxbrew/.linuxbrew/Cellar/qt@5/5.15.13_1/include/QtCore/qstring.h:832:31: note:   conversion of argument 1 would be ill-formed:
windowmanager.cpp:570:32: error: invalid conversion from 'WId' {aka 'long long unsigned int'} to 'const char*' [-fpermissive]
  570 |         existingWindows.remove(key);
      |                                ^~~
      |                                |
      |                                WId {aka long long unsigned int}
windowmanager.cpp:570:32: error: invalid conversion from 'WId' {aka 'long long unsigned int'} to 'const char*' [-fpermissive]
  570 |         existingWindows.remove(key);
      |                                ^~~
      |                                |
      |                                WId {aka long long unsigned int}
../../../../linuxbrew/.linuxbrew/Cellar/qt@5/5.15.13_1/include/QtCore/qstring.h:832:51: note:   initializing argument 1 of 'QString::QString(const char*)'
  832 |     inline QT_ASCII_CAST_WARN QString(const char *ch)
      |                                       ~~~~~~~~~~~~^~
In file included from ../../../../linuxbrew/.linuxbrew/Cellar/qt@5/5.15.13_1/include/QtCore/qvariant.h:47,
                 from ../../../../linuxbrew/.linuxbrew/Cellar/qt@5/5.15.13_1/include/QtCore/qlocale.h:43,
                 from ../../../../linuxbrew/.linuxbrew/Cellar/qt@5/5.15.13_1/include/QtCore/qtextstream.h:46:
../../../../linuxbrew/.linuxbrew/Cellar/qt@5/5.15.13_1/include/QtCore/qmap.h:911:58: note:   initializing argument 1 of 'int QMap<K, V>::remove(const Key&) [with Key = QString; T = QSize]'
  911 | Q_OUTOFLINE_TEMPLATE int QMap<Key, T>::remove(const Key &akey)
      |                                               ~~~~~~~~~~~^~~~
windowmanager.cpp: In member function 'virtual void WindowManager::paintEvent(QPaintEvent*)':
windowmanager.cpp:588:45: warning: unused parameter 'event' [-Wunused-parameter]
  588 | void WindowManager::paintEvent(QPaintEvent *event) {
      |                                ~~~~~~~~~~~~~^~~~~
make: *** [Makefile:2051: windowmanager.o] Error 1
make: *** Waiting for unfinished jobs....
