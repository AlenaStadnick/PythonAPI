package clickup.api.data;

import io.restassured.response.Response;
import lombok.Getter;
import lombok.Setter;

import java.util.HashMap;
import java.util.Map;

@Getter
@Setter
public class SharedTestData {
    private Response response;
    private String responseBody;
    private Map<String, String> responseData = new HashMap<>();

    public void setDataToMap(String key, String value) {
        responseData.put(key, value);
    }

    public String getDataFromMap(String key) {
        if (responseData.get(key) == null)
            return "";
        else
            return responseData.get(key);
    }
}
