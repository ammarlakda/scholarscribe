import { useQuery } from "react-query";
import "../../styles/components/response.scss";

export default function Response({ fetchData }) {
  const { isLoading, error, data } = useQuery("res", fetchData);

  if (isLoading) return "Loading...";

  if (error) {
    console.log(error);
    return "An error has occurred";
  }

  return (
    <div className="response">
      <h3>Response</h3>
      <div>{data}</div>
    </div>
  );
}
