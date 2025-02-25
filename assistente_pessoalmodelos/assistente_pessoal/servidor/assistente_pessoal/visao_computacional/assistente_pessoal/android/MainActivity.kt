import android.Manifest
import android.content.Context
import android.content.pm.PackageManager
import android.location.Location
import android.location.LocationListener
import android.location.LocationManager
import android.os.Bundle
import androidx.appcompat.app.AppCompatActivity
import androidx.core.app.ActivityCompat
import androidx.core.content.ContextCompat
import androidx.work.*
import kotlinx.coroutines.*
import okhttp3.*
import org.json.JSONObject
import java.io.IOException
import java.util.concurrent.TimeUnit

class MainActivity : AppCompatActivity() {
    // ... (mesmo código do aplicativo Android) ...
}

class LocationService : Service(), LocationListener {
    // ... (mesmo código do LocationService) ...
}

class DataSyncWorker(context: Context, workerParams: WorkerParameters) : Worker(context, workerParams) {
    // ... (mesmo código do DataSyncWorker) ...
}