#ifndef DIALOG_H
#define DIALOG_H

#include <QDialog>

QT_BEGIN_NAMESPACE
namespace Ui { class Dialog; }
QT_END_NAMESPACE

class Dialog : public QDialog
{
    Q_OBJECT

public:
    Dialog(QWidget *parent = nullptr);
    ~Dialog();

private slots:
    void on_btnClear_clicked();

    void on_chkBoxUnder_toggled(bool checked);

    void on_chkBoxBold_toggled(bool checked);

    void on_chkBoxItelic_clicked(bool checked);

private:
    Ui::Dialog *ui;
};
#endif // DIALOG_H
