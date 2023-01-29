import { useQuery } from "react-query";
import "../../styles/components/response.scss";

export default function Response({ fetchData }) {
  const { isLoading, error, data } = useQuery("res", fetchData);

  if (isLoading)
    return (
      <div className="response">
        <h3>Loading...</h3>
      </div>
    );

  if (error) {
    console.log(error);
    return (
      <div className="response">
        <h3>An Error Has Occured</h3>
      </div>
    );
  }

  return (
    <div className="response">
      <h3>Response</h3>
      <div>{data}</div>
    </div>
  );
}
