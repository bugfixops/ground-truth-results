package com.smlnskgmail.jaman.hashchecker.JacocoInstrument;

import android.content.BroadcastReceiver;
import android.content.Context;
import android.content.Intent;

import java.io.File;


public class SMSInstrumentedReceiver extends BroadcastReceiver {

    @Override
    public void onReceive(Context context, Intent intent) {
        // write the coverage file to the internal storage, which will not require any permissions
        // the output dir usually locates at: /data/data/#{app_package_name}/files/coverage.ec
        File coverageFile = new File(context.getFilesDir(), "coverage.ec");
        String coverageFilePath = coverageFile.getAbsolutePath();

        FinishListener mListener = new JacocoInstrumentation(coverageFilePath);

        if (mListener != null) {
            mListener.dumpIntermediateCoverage(coverageFilePath);
        }
    }
}
